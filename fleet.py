from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots_list = []
        self.weapons = [Weapon('Cannon', 25), Weapon('Blaster', 22), Weapon('Sabre', 33), Weapon('Laser Gun', 30)]

    def create_fleet(self):
        self.create_robot()


    def create_robot(self):
        robots_counter = 0
        while robots_counter != 3:
            self.robot = Robot(input('Enter robot name: '), 15)
            self.robot.active_weapon = self.fleet_weapon()
            self.robots_list.append(self.robot)
            robots_counter += 1

    def fleet_weapon(self):
        print('\n                     Choose a weapon:')
        print(f'1. {self.weapons[0].name}    2. {self.weapons[1].name}    3. {self.weapons[2].name}    4. {self.weapons[3].name}\n')
        print(f'If you select a wrong option - robot will not get any weapon!\n')
        weapon_input = input('Please, select weapon: ')
        if weapon_input == '1':
            self.robot.active_weapon = self.weapons[0]
            print(f"Robot {self.robot.name} is choosing {self.robot.active_weapon.name}!\n")
            return self.robot.active_weapon
        if weapon_input == '2':
            self.robot.active_weapon = self.weapons[1]
            print(f"Robot {self.robot.name} is choosing {self.robot.active_weapon.name}!\n")
            return self.robot.active_weapon
        if weapon_input == '3':
            self.robot.active_weapon = self.weapons[2]
            print(f"Robot {self.robot.name} is choosing {self.robot.active_weapon.name}!\n")
            return self.robot.active_weapon
        if weapon_input == '4':
            self.robot.active_weapon = self.weapons[3]
            print(f"Robot {self.robot.name} is choosing {self.robot.active_weapon.name}!\n")
            return self.robot.active_weapon
        else:
            self.robot.active_weapon = Weapon('feasts', 15)
            print(f"Robot {self.robot.name} didn't want to get a weapon. It's going to fight with {self.robot.active_weapon.name}!\n")
            return self.robot.active_weapon