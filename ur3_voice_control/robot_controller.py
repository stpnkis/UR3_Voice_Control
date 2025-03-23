import rtde_control  # Import knihovny pro řízení robota.
import rtde_receive  # Import knihovny pro příjem dat z robota
import math  # Import matematické knihovny pro výpočty.
import time  # Import knihovny pro práci s časem.
import configuration as config  # Import konfiguračního souboru jako config.

pi = math.pi  # Zkrácený zápis pro hodnotu Pi.

class RobotController:
    """
    Třída pro ovládání robota.

    Umožňuje vykonávání různých pohybových příkazů, jako je přesun do specifických pozic, uchopení a položení
    předmětů, pozdrav a otočení robota o 180 stupňů.
    """

    def __init__(self):
        """
        Inicializace spojení s robotem pomocí RTDE.
        """
        self.rtde_c = rtde_control.RTDEControlInterface(config.ROBOT_IP_ADDRESS)
        self.rtde_r = rtde_receive.RTDEReceiveInterface(config.ROBOT_IP_ADDRESS)

    def go_to_home_position(self):
        """
        Přesun robota do domovské pozice.
        """
        self.rtde_c.moveJ([0, -pi / 2, 0, -pi / 2, 0, 0])

    def go_to_position_a(self):
        """
        Přesun robota do bodu A.
        """
        self.rtde_c.moveJ([-0.995, -2.32, -0.79, -pi / 2, pi / 2, 0])

    def go_to_position_b(self):
        """
        Přesun robota do bodu B.
        """
        self.rtde_c.moveJ([1.14, -2.22, -0.75, -1.75, pi / 2, 0])

    def go_to_position_three(self):
        """
        Přesun robota do pozice 3.
        """
        self.rtde_c.moveJ([-pi / 4, -pi / 2, -pi / 2, -pi / 2, pi / 2, 0])

    def pick_up_object(self):
        """
        Sekvenční příkazy pro uchopení předmětu.
        """
        self.rtde_c.moveJ([0, -pi / 2, -pi / 2, -pi / 2, pi / 2, 0])
        time.sleep(0.5)  # Krátká pauza pro stabilizaci.
        self.rtde_c.moveL([0.2986, -0.11235, 0.13645, 2.221, -2.221, 0])
        time.sleep(0.5)  # Krátká pauza pro stabilizaci.
        self.rtde_c.moveL([0.2986, -0.11235, 0.31365, 2.221, -2.221, 0])

    def place_object(self):
        """
        Sekvenční příkazy pro položení předmětu.
        """
        self.rtde_c.moveJ([-pi / 4, -pi / 2, -pi / 2, -pi / 2, pi / 2, 0])
        time.sleep(0.5)  # Krátká pauza pro stabilizaci.
        self.rtde_c.moveL([0.1317, -0.2906, 0.13645, 1.202, -2.902, 0])
        time.sleep(0.5)  # Krátká pauza pro stabilizaci.
        self.rtde_c.moveL([0.1317, -0.2906, 0.31365, 1.202, -2.902, 0])

    def wave(self):
        """
        Provedení mávajícího pohybu jako pozdrav.
        """
        for i in range(2):  # Cyklus pro provedení mávajícího pohybu dvakrát.
            self.rtde_c.moveJ([0, -2.01, -0.61, -1.57, 0, 0])
            time.sleep(0.2) # Krátká pauza pro stabilizaci.
            self.rtde_c.moveJ([0, -1.84, -0.42, -1.57, 0, 0])
            time.sleep(0.2) # Krátká pauza pro stabilizaci.
            self.rtde_c.moveJ([0, -pi / 2, 0, -pi / 2, 0, 0])

    def rotate_180_degrees(self):
        """
        Otočení robota o 180 stupňů relativně k jeho současné pozici.
        """
        current_position = self.rtde_r.getActualQ()  # Získání současné pozice.
        target_position = list(current_position)  
        target_position[0] += math.pi   
        target_position[0] = (target_position[0] + math.pi) % (2 * math.pi) - math.pi 
        try:
            self.rtde_c.moveJ(target_position)
        except Exception as e:
            print(f"Nastala chyba při otáčení robota o 180 stupňů: {e}")
