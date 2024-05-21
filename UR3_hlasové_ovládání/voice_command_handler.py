import speech_recognition as sr  # Import knihovny pro rozpoznávání řeči.
import pygame  # Import knihovny pro práci se zvuky.
import configuration as config  # Import konfiguračního souboru jako config.

class VoiceCommandHandler:
    """
    Třída pro zpracování hlasových příkazů.
    
    Tato třída využívá knihovnu speech_recognition pro převod řeči na text a knihovnu pygame
    pro přehrání zvukového signálu jako upozornění.
    """

    def __init__(self):
        """
        Inicializuje rozpoznávač řeči a nastaví jazyk pro rozpoznávání podle konfiguračního souboru.
        Také inicializuje pygame mixer pro přehrávání zvuku při aktivaci.
        """
        self.recognizer = sr.Recognizer()  # Inicializace rozpoznávače řeči.
        self.language = config.LANGUAGE  # Nastavení jazyka rozpoznávání podle konfiguračního souboru.
        pygame.mixer.init()  # Inicializace pygame mixeru pro práci se zvukem.
        pygame.mixer.music.load(config.ACTIVATION_SOUND_PATH)  # Načtení zvukového souboru pro aktivaci.

    def get_voice_command(self):
        """
        Poslouchá a zpracovává hlasový příkaz od uživatele.
        
        Přehraje aktivační zvuk a poslouchá uživatelův příkaz, poté se ho pokouší převést na text.
        V případě chyby nebo nerozpoznání vrátí None.
        """
        with sr.Microphone() as source:  # Použití mikrofonu jako zdroje zvuku.
            pygame.mixer.music.play()  # Přehrání aktivačního zvuku.
            print("Poslouchám...")  # Informace pro uživatele.
            # Kontrola a přizpůsobení na úroveň okolního hluku.
            if config.DYNAMIC_MIC_ADJUSTMENT:
                self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source)  # Poslouchání a záznam zvuku.
                print("Zpracovávám...")  # Zpracování a převod zvuku na text.
                command = self.recognizer.recognize_google(audio, language=self.language)
                print(f"Příkaz: {command}")  # Výpis rozpoznaného příkazu.
                return command
            except sr.UnknownValueError:
                print("Nerozumím. Zkuste to znovu.")  # Ošetření nerozpoznání hlasu.
                return None
            except sr.RequestError as e:
                print(f"Chyba při požadavku na převod: {e}")  # Ošetření problému s převodem.
                return None

    def waiting_for_activation_command(self, activation_keyword=config.ACTIVATION_KEYWORD):
        """
        Čeká na aktivační příkaz definovaný v konfiguračním souboru.
        
        Vrací True, pokud byl aktivační příkaz rozpoznán, v opačném případě False.
        """
        print("Čekám na aktivační příkaz...")  # Informace pro uživatele o čekání na příkaz.
        with sr.Microphone() as source:  # Použití mikrofonu jako zdroje zvuku.
            # Kontrola a přizpůsobení na úroveň okolního hluku.
            if config.DYNAMIC_MIC_ADJUSTMENT:
                self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)  # Poslouchání a záznam zvuku.
            try:
                text = self.recognizer.recognize_google(audio, language=self.language)
                if activation_keyword.lower() in text.lower():  # Kontrola obsahu aktivačního klíčového slova.
                    print("Zahajuji převod hlasu na text...")  # Informace o rozpoznání aktivačního příkazu.
                    return True
            except sr.UnknownValueError:
                # Ignorování chyby nerozpoznání.
                pass
            except sr.RequestError as e:
                print(f"Chyba připojení k službě pro rozpoznávání řeči: {e}")  # Ošetření chyby při převodu.
            return False
