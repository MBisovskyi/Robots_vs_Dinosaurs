from robot import Robot
from dinosaur import Dinosaur

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

dinosaur = Dinosaur('Arghhh', 25)
robot = Robot('TasteOfSteel')