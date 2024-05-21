# IP adresa robota 
ROBOT_IP_ADDRESS = "192.168.31.129"
# Klíčové slovo pro aktivaci hlasového ovládání 
ACTIVATION_KEYWORD = "robot"
# Jazyk pro rozpoznávání hlasu (např. angličtina - "en-US", čeština - "cs-CZ" více na https://cloud.google.com/speech-to-text/docs/languages)
LANGUAGE = "cs-CZ"
# Cesta k zvukovému souboru pro signalizaci aktivace hlasového ovládání
ACTIVATION_SOUND_PATH = "Aktivacnizvuk.wav"
# Povolit dynamickou úpravu citlivosti mikrofonu pro odstranění šumu (True/False)
# Když je nastaveno na True, systém se automaticky přizpůsobí úrovni hluku v prostředí
DYNAMIC_MIC_ADJUSTMENT = True
# Počet pokusů pro neplatné příkazy
# Definuje, kolikrát může uživatel opakovat pokus o zadání platného hlasového příkazu
INVALID_COMMAND_ATTEMPTS = 2
