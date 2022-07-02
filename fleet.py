from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.fleet = []
        self.weapons = [Weapon('Cannon', 25), Weapon('Blaster', 20), Weapon('Sabre', 35), Weapon('Laser Gun', 30)]

    def create_fleet(self):
        self.create_robot()


    def create_robot(self):
        robots_counter = 0
        while robots_counter != 3:
            self.robot = Robot(input('Enter robot name: '), 15)
            self.robot.active_weapon = self.choose_weapon()
            self.fleet.append(self.robot.name)
            robots_counter += 1

    def choose_weapon(self):
        print('\n                     Choose a weapon:')
        print(f'1. {self.weapons[0].name}    2. {self.weapons[1].name}    3. {self.weapons[2].name}    4. {self.weapons[3].name}\n')
        print(f'If you select a wrong option - robot will not get any weapon!\n')
        weapon_input = input('Please, select weapon: ')
        print()
        if weapon_input == '1':
            self.robot.active_weapon = self.weapons[0]
            return self.robot.active_weapon
        if weapon_input == '2':
            self.robot.active_weapon = self.weapons[1]
            return self.robot.active_weapon
        if weapon_input == '3':
            self.robot.active_weapon = self.weapons[2]
            return self.robot.active_weapon
        if weapon_input == '4':
            self.robot.active_weapon = self.weapons[3]
            return self.robot.active_weapon
        else:
            self.robot.active_weapon = Weapon('Feast', 15)
            return self.robot.active_weapon