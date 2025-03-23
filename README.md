# Bachelor's Thesis: Voice Control of UR3 Collaborative Robot

This repository contains code created for a bachelor's thesis focused on voice control of the UR3 collaborative robot. The repository is divided into two main parts: the program for controlling the robot via voice commands and code for speech-to-text conversion using three different systems.

## Repository Structure

### ur3_voice_control

This section contains the code for controlling the UR3 collaborative robot through voice commands. It consists of four modules:

- **main.py**: Main executable script integrating all modules.
- **robot_controller.py**: Module responsible for controlling the UR3 robot.
- **voice_command_handler.py**: Module handling voice command processing.
- **configuration.py**: Configuration file containing parameters and settings for robot control.

### speech_recognition

This section contains scripts for speech-to-text conversion using various services:

- **Google_Speech_Recognition/Google_Speech_Recognition.py**: Script using Google Web Speech API for speech-to-text conversion.
- **Whisper/Whisper.py**: Script using the Whisper model for speech-to-text conversion.
- **IBM_Watson_Speech_to_Text/IBM_Watson_Speech_to_Text.py**: Script using IBM Watson Speech to Text API for speech-to-text conversion.

## Installation and Usage

### UR3 Robot Voice Control

1. Clone this repository:
    ```bash
    git clone https://github.com/stpnkis/UR3_Voice_Control.git
    cd UR3_Voice_Control/ur3_voice_control
    ```

2. Install necessary dependencies:
    ```bash
    pip install -r ur3_voice_control/requirements.txt
    ```

3. Configure parameters in `configuration.py` according to your needs.

4. Run the main script:
    ```bash
    python ur3_voice_control/main.py
    ```

### Speech-to-Text Conversion

1. Install necessary dependencies for each script:

    - Google Speech Recognition:
        ```bash
        pip install -r speech_recognition/Google_Speech_Recognition/requirements.txt
        ```

    - Whisper:
        ```bash
        pip install -r speech_recognition/Whisper/requirements.txt
        ```

    - IBM Watson Speech to Text:
        ```bash
        pip install -r speech_recognition/IBM_Watson_Speech_to_Text/requirements.txt
        ```

2. Run individual scripts for speech-to-text conversion:

    - Google Speech Recognition:
        ```bash
        python speech_recognition/Google_Speech_Recognition/Google_Speech_Recognition.py
        ```

    - Whisper:
        ```bash
        python speech_recognition/Whisper/Whisper.py
        ```

    - IBM Watson Speech to Text:
        ```bash
        python speech_recognition/IBM_Watson_Speech_to_Text/IBM_Watson_Speech_to_Text.py
        ```

