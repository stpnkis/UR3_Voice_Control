# Bakalářská práce: Ovládání kolaborativního robota UR3 pomocí hlasu

Tento repozitář obsahuje kódy vytvořené pro bakalářskou práci zaměřenou na ovládání kolaborativního robota UR3 pomocí hlasu. Repozitář je rozdělen do dvou hlavních částí: ovládání robota a převádění řeči na text.

## Struktura repozitáře

### UR3_voice_control

Tato část obsahuje kódy pro ovládání kolaborativního robota UR3 pomocí hlasových příkazů. Skládá se ze čtyř modulů:

- **main.py**: Hlavní spouštěcí skript, který integruje všechny moduly.
- **robot_controller.py**: Modul pro řízení robota UR3.
- **voice_command_handler.py**: Modul pro zpracování hlasových příkazů.
- **configuration.py**: Konfigurační soubor obsahující nastavení a parametry pro ovládání robota.

### speech_recognition

Tato část obsahuje kódy pro převádění řeči na text pomocí různých služeb:

- **google_speech_recognition/Google_Speech_Recognition.py**: Kód pro převádění řeči na text pomocí Google Web Speech API.
- **whisper/Whisper.py**: Kód pro převádění řeči na text pomocí modelu Whisper.
- **ibm_watson_speech_to_text/IBM_Watson_Speech_to_Text.py**: Kód pro převádění řeči na text pomocí služby IBM Watson Speech to Text API.

## Instalace a použití

### Ovládání robota UR3

1. Klonujte tento repozitář:
    ```bash
    git clone https://github.com/vaseuzivatelskejmeno/robot-voice-control.git
    cd robot-voice-control
    ```

2. Nainstalujte potřebné závislosti:
    ```bash
    pip install -r UR3_voice_control/requirements.txt
    ```

3. Konfigurujte parametry v `configuration.py` podle vašich potřeb.

4. Spusťte hlavní program:
    ```bash
    python UR3_voice_control/main.py
    ```

### Převádění řeči na text

1. Nainstalujte potřebné závislosti pro jednotlivé skripty:

    - Google Speech Recognition:
        ```bash
        pip install -r speech_recognition/google_speech_recognition/requirements.txt
        ```

    - Whisper:
        ```bash
        pip install -r speech_recognition/whisper/requirements.txt
        ```

    - IBM Watson Speech to Text:
        ```bash
        pip install -r speech_recognition/ibm_watson_speech_to_text/requirements.txt
        ```

2. Spusťte jednotlivé skripty pro převod řeči na text:
    - Google Speech Recognition:
        ```bash
        python speech_recognition/google_speech_recognition/Google_Speech_Recognition.py
        ```
    - Whisper:
        ```bash
        python speech_recognition/whisper/Whisper.py
        ```
    - IBM Watson Speech to Text:
        ```bash
        python speech_recognition/ibm_watson_speech_to_text/IBM_Watson_Speech_to_Text.py
        ```

## Licence

Tento projekt je licencován pod MIT licencí - viz soubor [LICENSE](LICENSE) pro více informací.

## Kontakt

Pro další informace kontaktujte autora na [email@example.com](mailto:email@example.com).
