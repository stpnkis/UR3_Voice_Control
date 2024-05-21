from voice_command_handler import VoiceCommandHandler  # Import třídy pro zpracování hlasových příkazů.
from robot_controller import RobotController  # Import třídy pro ovládání robota.
import configuration as config  # Import konfiguračního souboru jako config.

def main():
    """
    Hlavní funkce programu pro hlasové ovládání kolaborativního robota.
    
    Program nejprve inicializuje ovladače pro robota a pro zpracování hlasových příkazů.
    Následně neustále čeká na aktivaci pomocí aktivačního příkazu definovaného uživatelem.
    Po aktivaci přijímá hlasové příkazy a spouští příslušné funkce robota.
    """
    # Inicializace ovladače robota a zpracování hlasových příkazů.
    robot_controller = RobotController()
    voice_handler = VoiceCommandHandler()

    while True:
        # Čekání na aktivační příkaz.
        if voice_handler.waiting_for_activation_command(config.ACTIVATION_KEYWORD):
            # Získání hlasového příkazu a jeho zpracování.
            for _ in range(config.INVALID_COMMAND_ATTEMPTS):  # Počet pokusů definovaný uživatelem pro neplatné příkazy.
                command = voice_handler.get_voice_command()
                if command:
                    command_lower = command.lower()  # Převod příkazu na malá písmena pro normalizaci.
                    match command_lower:
                        case _ if "domovská pozice" in command_lower:
                            robot_controller.go_to_home_position()
                            print("Kobot se nachází v domovské pozici.")
                            break
                        case _ if "běž do bodu a" in command_lower:
                            robot_controller.go_to_position_a()
                            print("Kobot se nachází v bodě A.")
                            break
                        case _ if "přesuň se do bodu b" in command_lower:
                            robot_controller.go_to_position_b()
                            print("Kobot se nachází v bodě B.")
                            break
                        case _ if "běž do pozice 3" in command_lower:
                            robot_controller.go_to_position_three()
                            print("Kobot se nachází v pozici 3.")
                            break
                        case _ if "polož předmět" in command_lower:
                            robot_controller.place_object()
                            print("Kobot položil předmět.")
                            break
                        case _ if "zvedni předmět" in command_lower:
                            robot_controller.pick_up_object()
                            print("Kobot uchopil předmět.")
                            break
                        case _ if "pozdrav" in command_lower:
                            robot_controller.wave()
                            print("Zdravím.")
                            break
                        case _ if "otoč se o 180" in command_lower:
                            robot_controller.rotate_180_degrees()
                            print("Kobot se otočil o 180 stupňů.")
                            break
                        case _ if "vypnout" in command_lower:
                            print("Program se vypíná.")
                            return
                        case _:
                            print("Nerozpoznaný příkaz. Zkuste to znovu.")
                else:
                    break

if __name__ == "__main__":
    main()
