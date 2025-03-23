import speech_recognition as sr

def speech_to_text():
    """Funkce pro převod řeči na text pomocí knihovny SpeechRecognition a Google Speech Recognition."""
    # Vytvoření instance rozpoznávače
    recognizer = sr.Recognizer()

    # Použití mikrofonu jako zdroje zvuku
    with sr.Microphone() as source:
        print("Nastavuji mikrofon... Prosím, chvíli počkejte.")
        recognizer.adjust_for_ambient_noise(source)
        print("Mikrofon je nastaven. Nyní prosím, řekněte něco.")
        
        # Zachycení zvuku z mikrofonu
        audio = recognizer.listen(source)
        print("Nahrávka dokončena. Zpracovávám nahrávku...")

        try:
            # Rozpoznání řeči pomocí Google Speech Recognition
            text = recognizer.recognize_google(audio, language="cs-CZ")
            print("Rozpoznaný text: " + text)
        except sr.UnknownValueError:
            print("Promiňte, nerozumím.")
        except sr.RequestError:
            print("Chyba při komunikaci se službou rozpoznávání řeči.")

if __name__ == "__main__":
    speech_to_text()
