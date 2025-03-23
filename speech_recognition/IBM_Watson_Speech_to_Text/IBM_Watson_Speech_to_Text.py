import os
import pyaudio
import wave
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Definice API klíče a URL pro službu IBM Watson Speech to Text
API_KEY = "q1w3H6UDotugwPRKj_ctG5bGkC2o858rjp2wGt1r7Vh5"
SERVICE_URL = "https://api.eu-de.speech-to-text.watson.cloud.ibm.com/instances/f5025468-31e8-47b3-b511-a5714a2b0167"

# Inicializace služby IBM Watson Speech to Text
authenticator = IAMAuthenticator(API_KEY)
speech_to_text = SpeechToTextV1(authenticator=authenticator)
speech_to_text.set_service_url(SERVICE_URL)

def record_audio(filename, duration=5):
    """ Funkce pro nahrávání audia z mikrofonu a ukládání do WAV souboru. """
    # Nastavení parametrů pro nahrávání
    chunk_size = 1024
    audio_format = pyaudio.paInt16
    channels = 1
    sample_rate = 44100
    
    # Nahrávání audio záznamu z mikrofonu
    p_audio = pyaudio.PyAudio()
    stream = p_audio.open(format=audio_format, channels=channels, rate=sample_rate, input=True, frames_per_buffer=chunk_size)
    frames = [stream.read(chunk_size) for _ in range(int(sample_rate / chunk_size * duration))]
    stream.stop_stream()
    stream.close()
    p_audio.terminate()
    
    # Ukládání nahrávky
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p_audio.get_sample_size(audio_format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

def convert_speech_to_text(audio_file_path):
    """ Funkce pro převod řeči na text pomocí IBM Watson Speech to Text API. """
    with open(audio_file_path, 'rb') as audio_file:
        result = speech_to_text.recognize(audio=audio_file, content_type='audio/wav', model='cs-CZ_Telephony').get_result()
    return result.get('results')[0]['alternatives'][0]['transcript'].strip() if result.get('results') else "Řeč nebyla rozpoznána"

def main():
    """ Hlavní funkce, koordinuje nahrávání audio a jeho převod na text. """
    try:
        audio_file = "audio.wav"
        print("Nahrávám zvuk...")
        record_audio(audio_file)
        print("Převádím řeč na text...")
        transcription = convert_speech_to_text(audio_file)
        print("Řekl jste:", transcription)
    except Exception as e:
        print("Došlo k chybě:", e)

if __name__ == "__main__":
    main()
