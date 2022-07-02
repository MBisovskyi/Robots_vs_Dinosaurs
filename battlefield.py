from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.battle = True
        self.dinosaur = None
        self.robot = None
        self.fleet = Fleet()
        self.herd = []

    def run_games(self):
        user_choice = self.game_mode()
        if user_choice == '1':
            self.robot_dinosaur()
        elif user_choice == '2':
            self.fleet_herd()

    def game_mode(self):
        print("                     GAME MODE:")
        user_choice = input("1. Robot vs Dinosaur            2. Fleet vs Nerd\nSelect option: ")
        return user_choice  

    def display_welcome(self):
        print(f"\n                    BATTLE\n         Robot: {self.robot.name.upper()}  vs  Dino: {self.dinosaur.name.upper()}\n")
        print(f"I'll put $100 that Robot {self.robot.name} will handle this easily!\n")
    
    def battle_phase(self):
        while self.battle == True:
            if self.robot.health > 0:
                self.dinosaur.attack(self.robot.name)
                self.robot.health = self.robot.health - self.dinosaur.attack_power
                if self.robot.health <= 0:
                    print(f"Robot {self.robot.name} is down!\n")
                    break
            if self.dinosaur.health > 0:
                self.robot.choose_weapon()
                self.robot.attack(self.dinosaur)
                self.dinosaur.health = self.dinosaur.health - self.robot.active_weapon.attack_power
                if self.dinosaur.health <= 0:
                    print(f"Dino {self.dinosaur.name} is smashed!\n")
                    break
            else:
                self.battle = False

    def display_winner(self):
            if self.robot.health <= 0:
                print(f"Dino {self.dinosaur.name} wins!\n")
                print(f'It was an epic battle, which defined Robot {self.robot.name} as a looser... Oh, my bad. Defined him as DEAD Robot {self.robot.name}!\n')
            elif self.dinosaur.health <= 0:
                print(f"Robot {self.robot.name} wins! Nothing unpredictable.\n")
                print(f'Like I said, Dino {self.dinosaur.name} is an easy opponent for Robot {self.robot.name}. By the way, where is my winning bet?!\n')

    def create_robot(self):
        self.robot = Robot(input("\nEnter Robot name: "), 15)
        return self.robot

    def create_dinosaur(self):
        self.dinosaur = Dinosaur(input("Enter Dino name: "), 25)
        return self.dinosaur

    def robot_dinosaur(self):
        self.create_robot()
        self.create_dinosaur()
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
    
    def fleet_herd(self):
        self.fleet.create_fleet()