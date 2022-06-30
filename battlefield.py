from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.action = True


    def run_games(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print(" ")
        print("This battle will be epic! Are you ready to make a bet?")
        print(f"I'll put $100 that Robot {robot.name} will handle this easily!")
        print(" ")
    
    def battle_phase(self):
        while self.action == True:
            if robot.health > 0:
                dinosaur.attack(robot.name)
                robot.health = robot.health - dinosaur.attack_power
                print(f'Robot {robot.name} has {robot.health} health remaining!')
                print(" ")
                if robot.health <= 0:
                    break
            if dinosaur.health > 0:
                
                robot.attack(dinosaur.name)
                dinosaur.health = dinosaur.health - robot.active_weapon.attack_power
                print(f'Dinosaur {dinosaur.name} has {dinosaur.health} health remaining!')
                print(" ")
                if dinosaur.health <= 0:
                    break
            else:
                self.action = False

    def display_winner(self):
            if robot.health <= 0:
                print(f"{dinosaur.name} wins!")
                print(" ")
            elif dinosaur.health <= 0:
                print(f"{robot.name} wins! Nothing unpredictable.")
                print(" ")
                
    def robot_weapon(self):
        print("1. Cannon - damage 30        2. Blaster - damage 20      3. Sabre - damage 35")
        user_ipnut = int(input(f'Select a weapon: '))
        if user_ipnut == 1:
            self.active_weapon = cannon
        elif user_ipnut == 2:
            self.active_weapon = blaster
        elif user_ipnut == 3:
            self.active_weapon = sabre

dinosaur = Dinosaur('Arghhh', 25)
robot = Robot('TasteOfSteel')
cannon = Weapon('Cannon', 30)
blaster = Weapon('Blaster', 20)
sabre = Weapon('Sabre', 35)
