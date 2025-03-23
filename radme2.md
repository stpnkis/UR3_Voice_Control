# Bachelor's Thesis: Voice Control of the UR3 Collaborative Robot

This repository contains the code developed for a bachelor's thesis focused on controlling the UR3 collaborative robot using voice commands. The repository is divided into two main parts: voice-controlled robot application and speech-to-text conversion scripts utilizing three different systems.

## Repository Structure

### UR3_Voice_Control

This section contains the code for controlling the UR3 collaborative robot through voice commands. It consists of four modules:

- **main.py**: The main execution script integrating all modules.
- **robot_controller.py**: Module responsible for controlling the UR3 robot.
- **voice_command_handler.py**: Module handling voice command processing.
- **configuration.py**: Configuration file containing parameters and settings for robot control.

### Speech_Recognition

This section contains scripts for speech-to-text conversion using various services:

- **Google_Speech_Recognition/Google_Speech_Recognition.py**: Script using Google Web Speech API for speech-to-text conversion.
- **Whisper/Whisper.py**: Script using the Whisper model for speech-to-text conversion.
- **IBM_Watson_Speech_to_Text/IBM_Watson_Speech_to_Text.py**: Script using IBM Watson Speech to Text API for speech-to-text conversion.

## Installation and Usage

### UR3 Robot Voice Control

1. Clone this repository:
    ```bash
    git clone https://github.com/stpnkis/BP_UR3_hlasove_ovladani.git
    cd BP_UR3_hlasove_ovladani/UR3_Voice_Control
    ```

2. Install required dependencies:
    ```bash
    pip install -r UR3_Voice_Control/requirements.txt
    ```

3. Configure parameters in `configuration.py` according to your needs.

4. Run the main script:
    ```bash
    python UR3_Voice_Control/main.py
    ```

### Speech-to-Text Conversion

1. Install required dependencies for each script:

    - Google Speech Recognition:
        ```bash
        pip install -r Speech_Recognition/Google_Speech_Recognition/requirements.txt
        ```

    - Whisper:
        ```bash
        pip install -r Speech_Recognition/Whisper/requirements.txt
        ```

    - IBM Watson Speech to Text:
        ```bash
        pip install -r Speech_Recognition/IBM_Watson_Speech_to_Text/requirements.txt
        ```

2. Run the respective scripts for speech-to-text conversion:

    - Google Speech Recognition:
        ```bash
        python Speech_Recognition/Google_Speech_Recognition/Google_Speech_Recognition.py
        ```

    - Whisper:
        ```bash
        python Speech_Recognition/Whisper/Whisper.py
        ```

    - IBM Watson Speech to Text:
        ```bash
        python Speech_Recognition/IBM_Watson_Speech_to_Text/IBM_Watson_Speech_to_Text.py
        ```

