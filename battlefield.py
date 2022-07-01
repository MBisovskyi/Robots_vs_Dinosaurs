from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.battle = True

    def run_games(self):
        user_choice = self.game_mode()
        if user_choice == '1':
            self.display_welcome()
            self.battle_phase()
            self.display_winner()
        elif user_choice == '2':
            self.create_fleet()
            self.create_herd()

    def game_mode(self):
        print("                     GAME MODE:")
        user_choice = input("1. Robot vs Dinosaur            2. Fleet vs Nerd \n     \nSelect option: ")
        return user_choice     

    def create_fleet(self):
        self.robot1 = Robot(input("First Robot name: "))
        self.robot2 = Robot(input("Second Robot name: "))
        self.robot3 = Robot(input("Third Robot name: "))
        print(f"\nFleet squad is:\n\n1. Robot {self.robot1.name} weapon: {weapon1.name} - damage: {weapon1.attack_power}\n2. Robot {self.robot2.name} weapon: {weapon2.name} - damage: {weapon2.attack_power}\n3. Robot {self.robot3.name} weapon: {weapon3.name} - damage: {weapon3.attack_power}\n\nNice choice!\n")

    def create_herd(self):
        self.dinosaur1 = Dinosaur(input("First Dino name: "), 25)
        self.dinosaur2 = Dinosaur(input("Second Dino name: "), 27)
        self.dinosaur3 = Dinosaur(input("Third Dino name: "), 22)
        print(f"\nHerd squad is:\n\n1. Dino {self.dinosaur1.name} - damage: {self.dinosaur1.attack_power}\n2. Dino {self.dinosaur2.name} - damage: {self.dinosaur2.attack_power}\n3. Dino {self.dinosaur3.name} - damage: {self.dinosaur3.attack_power}\n\nThey are huge!\n")

    def display_welcome(self):
        print(" ")
        print("This battle will be epic! Are you ready to make a bet?")
        print(f"I'll put $100 that Robot {robot.name} will handle this easily!")
        print(" ")
    
    def battle_phase(self):
        while self.battle == True:
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
                self.battle = False

    def fleet_vs_herd_battle(self):
        while self.battle == True:
            pass
                

    def display_winner(self):
            if robot.health <= 0:
                print(f"{dinosaur.name} wins!")
                print(" ")
            elif dinosaur.health <= 0:
                print(f"{robot.name} wins! Nothing unpredictable.")
                print(" ")

dinosaur = Dinosaur('Arghhh', 25)
robot = Robot('TasteOfSteel')
weapon1 = Weapon('Cannon', 30)
weapon2 = Weapon('Blaster', 20)
weapon3 = Weapon('Sabre', 35)

