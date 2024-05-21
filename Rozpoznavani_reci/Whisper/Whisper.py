import argparse
import io
import os
import speech_recognition as sr
import whisper
import torch

from datetime import datetime, timedelta, timezone
from queue import Queue
from tempfile import NamedTemporaryFile

def get_arguments() -> argparse.Namespace:
    """Zpracuje argumenty příkazové řádky pro konfiguraci rozpoznávání řeči."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="medium", choices=["tiny", "base", "small", "medium", "large"],
                        help="Model k použití")
    parser.add_argument("--non_english", action='store_true', help="Nepoužívat anglický model.")
    parser.add_argument("--energy_threshold", default=1000, type=int, help="Hladina energie pro detekci mikrofonem.")
    parser.add_argument("--record_timeout", default=2, type=float, help="Délka nahrávky v sekundách.")
    parser.add_argument("--phrase_timeout", default=3, type=float, help="Délka pauzy mezi frázemi než to považujeme za nový řádek v přepisu.")
    return parser.parse_args()

def setup_microphone(recorder: sr.Recognizer, energy_threshold: int) -> sr.Microphone:
    """Nastaví mikrofon s uvedenou prahovou hodnotou energie."""
    recorder.energy_threshold = energy_threshold
    recorder.dynamic_energy_threshold = False
    return sr.Microphone(sample_rate=16000)

def record_callback(_, audio: sr.AudioData, data_queue: Queue):
    """Callback funkce pro zpracování audio dat a vložení do fronty."""
    data = audio.get_raw_data()
    data_queue.put(data)

def transcribe_audio(recorder: sr.Recognizer, data_queue: Queue, audio_model, source: sr.Microphone, 
                     record_timeout: float, phrase_timeout: float):
    """Zajišťuje nahrávání a přepis zvuku."""
    temp_file = NamedTemporaryFile().name
    transcription = ['']
    phrase_time = None
    last_sample = bytes()

    recorder.listen_in_background(source, lambda _, audio: record_callback(_, audio, data_queue), 
                                  phrase_time_limit=record_timeout)

    print("Mluvte.\n")
    
    while True:
        try:
            now = datetime.now(timezone.utc)
            if not data_queue.empty():
                phrase_complete = False
                if phrase_time and now - phrase_time > timedelta(seconds=phrase_timeout):
                    last_sample = bytes()
                    phrase_complete = True

                phrase_time = now
                while not data_queue.empty():
                    data = data_queue.get()
                    last_sample += data

                audio_data = sr.AudioData(last_sample, source.SAMPLE_RATE, source.SAMPLE_WIDTH)
                wav_data = io.BytesIO(audio_data.get_wav_data())

                with open(temp_file, 'w+b') as f:
                    f.write(wav_data.read())

                result = audio_model.transcribe(temp_file, fp16=torch.cuda.is_available())
                text = result['text'].strip()

                if phrase_complete:
                    transcription.append(text)
                else:
                    transcription[-1] = text

                os.system('cls' if os.name == 'nt' else 'clear')
                for line in transcription:
                    print(line)
                print('', end='', flush=True)
        except KeyboardInterrupt:
            break

    print("\n\nŘekl jste:")
    for line in transcription:
        print(line)

def main():
    """Hlavní funkce, která spouští proces rozpoznávání řeči."""
    args = get_arguments()
    data_queue = Queue()
    recorder = sr.Recognizer()
    source = setup_microphone(recorder, args.energy_threshold)

    audio_model = whisper.load_model(args.model)
    print(f"Nahraný model: {args.model}")

    with source:
        recorder.adjust_for_ambient_noise(source)

    transcribe_audio(recorder, data_queue, audio_model, source, args.record_timeout, args.phrase_timeout)

if __name__ == "__main__":
    main()
