from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.action = True
        self.fleet = []
        self.herd = []

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
        robot1 = Robot(input("First Robot name: "))
        self.fleet.append(robot1.name)
        robot2 = Robot(input("Second Robot name: "))
        self.fleet.append(robot2.name)
        robot3 = Robot(input("Third Robot name: "))
        self.fleet.append(robot3.name)
        print(f"\nFleet squad is:\n\n1. Robot {self.fleet[0]}\n2. Robot {self.fleet[1]}\n3. Robot {self.fleet[2]}\n\nNice choice!\n")
        

    def create_herd(self):
        dinosaur1 = Dinosaur(input("First Dino name: "), 25)
        self.herd.append(dinosaur1.name)
        dinosaur2 = Dinosaur(input("Second Dino name: "), 25)
        self.herd.append(dinosaur2.name)
        dinosaur3 = Dinosaur(input("Third Dino name: "), 25)
        self.herd.append(dinosaur3.name)
        print(f"\nHerd squad is:\n\n1. Dino {self.herd[0]}\n2. Dino {self.herd[1]}\n3. Dino {self.herd[2]}\n\nThey are huge!\n")


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

