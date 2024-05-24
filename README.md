# Bakalářská práce: Ovládání kolaborativního robota UR3 pomocí hlasu

Tento repozitář obsahuje kódy vytvořené pro bakalářskou práci zaměřenou na ovládání kolaborativního robota UR3 pomocí hlasu. Repozitář je rozdělen do dvou hlavních částí: program pro ovládání robota hlasem a kódy pro převod řeči na text pomocí 3 různých systémů.

## Struktura repozitáře

### UR3_hlasove_ovladani

Tato část obsahuje kódy pro ovládání kolaborativního robota UR3 pomocí hlasových příkazů. Skládá se ze čtyř modulů:

- **main.py**: Hlavní spouštěcí skript, který integruje všechny moduly.
- **robot_controller.py**: Modul pro řízení robota UR3.
- **voice_command_handler.py**: Modul pro zpracování hlasových příkazů.
- **configuration.py**: Konfigurační soubor obsahující nastavení a parametry pro ovládání robota.

### Rozpoznavani_reci

Tato část obsahuje kódy pro převádění řeči na text pomocí různých služeb:

- **Google_Speech_Recognition/Google_Speech_Recognition.py**: Kód pro převádění řeči na text pomocí Google Web Speech API.
- **Whisper/Whisper.py**: Kód pro převádění řeči na text pomocí modelu Whisper.
- **IBM_Watson_Speech_to_Text/IBM_Watson_Speech_to_Text.py**: Kód pro převádění řeči na text pomocí služby IBM Watson Speech to Text API.

## Instalace a použití

### Ovládání robota UR3

1. Klonujte tento repozitář:
    ```bash
    git clone https://github.com/stpnkis/BP_UR3_hlasove_ovladani.git
    cd BP_UR3_hlasove_ovladani\UR3_hlasove_ovladani
    ```

2. Nainstalujte potřebné závislosti:
    ```bash
    pip install -r UR3_hlasove_ovladani/requirements.txt
    ```

3. Konfigurujte parametry v `configuration.py` podle vašich potřeb.

4. Spusťte hlavní program:
    ```bash
    python UR3_hlasove_ovladani/main.py
    ```

### Převádění řeči na text

1. Nainstalujte potřebné závislosti pro jednotlivé skripty:

    - Google_Speech_Recognition:
        ```bash
        pip install -r Rozpoznavani_reci/Google_Speech_Recognition/requirements.txt
        ```

    - Whisper:
        ```bash
        pip install -r Rozpoznavani_reci/Whisper/requirements.txt
        ```

    - IBM_Watson_Speech_to_Text:
        ```bash
        pip install -r Rozpoznavani_reci/IBM_Watson_Speech_to_Text/requirements.txt
        ```

2. Spusťte jednotlivé skripty pro převod řeči na text:
    - Google_Speech_Recognition:
        ```bash
        python Rozpoznavani_reci/Google_Speech_Recognition/Google_Speech_Recognition.py
        ```
    - Whisper:
        ```bash
        python Rozpoznavani_reci/Whisper/Whisper.py
        ```
    - IBM_Watson_Speech_to_Text:
        ```bash
        python Rozpoznavani_reci/IBM_Watson_Speech_to_Text/IBM_Watson_Speech_to_Text.py
        ```




