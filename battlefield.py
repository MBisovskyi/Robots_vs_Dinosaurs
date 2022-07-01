from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.battle = True
        self.dinosaur = None
        self.robot = None

    def run_games(self):
        user_choice = self.game_mode()
        if user_choice == '1':
            self.create_robot()
            self.create_dinosaur()
            self.display_welcome()
            self.battle_phase()
            self.display_winner()
        elif user_choice == '2':
            self.create_fleet()
            self.create_herd()
            self.round_one()
            self.round_two()
            self.round_three()
            self.fleet_herd_final_display()

    def game_mode(self):
        print("                     GAME MODE:")
        user_choice = input("1. Robot vs Dinosaur            2. Fleet vs Nerd\nSelect option: ")
        return user_choice  

    def create_fleet(self):
        self.robot1 = Robot(input("First Robot name: "))
        self.robot2 = Robot(input("Second Robot name: "))
        self.robot3 = Robot(input("Third Robot name: "))
        print(f"\nFleet squad is:\n\n1. Robot {self.robot1.name}\n2. Robot {self.robot2.name}\n3. Robot {self.robot3.name}\n\nNice choice!\n")

    def create_herd(self):
        self.dinosaur1 = Dinosaur(input("First Dino name: "), 25)
        self.dinosaur2 = Dinosaur(input("Second Dino name: "), 27)
        self.dinosaur3 = Dinosaur(input("Third Dino name: "), 22)
        print(f"\nHerd squad is:\n\n1. Dino {self.dinosaur1.name} - damage: {self.dinosaur1.attack_power}\n2. Dino {self.dinosaur2.name} - damage: {self.dinosaur2.attack_power}\n3. Dino {self.dinosaur3.name} - damage: {self.dinosaur3.attack_power}\n\nThey are huge!\n")

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
                self.robot.choose_weapon(self.dinosaur)
                self.robot.attack(self.dinosaur)
                self.dinosaur.health = self.dinosaur.health - self.robot.active_weapon.attack_power
                if self.dinosaur.health <= 0:
                    print(f"Dino {self.dinosaur.name} is smashed!\n")
                    break
            else:
                self.battle = False

    def round_one(self):
        self.battle_one = True
        print(f"                    ROUND 1\n                 {self.robot1.name.upper()} vs {self.dinosaur1.name.upper()}\n")
        while self.battle_one == True:
            self.dinosaur1.attack(self.robot1.name)
            self.robot1.health = self.robot1.health - self.dinosaur1.attack_power
            if self.robot1.health > 0:
                print(f'Robot {self.robot1.name} has {self.robot1.health} health remaining!\n')
            if self.robot1.health <= 0:
                print(f"\nRobot {self.robot1.name} is killed!\n")
                break
            if self.dinosaur1.health > 0:
                self.robot1.attack(self.dinosaur1.name)
                self.dinosaur1.health = self.dinosaur1.health - self.robot1.active_weapon.attack_power
                if self.dinosaur1.health > 0:
                    print(f'Dino {self.dinosaur1.name} has {self.dinosaur1.health} health remaining!\n')
                if self.dinosaur1.health <= 0:
                    print(f"\nDino {self.dinosaur1.name} is killed!\n")
                    break

    def round_two(self):
        self.battle_two = True
        print(f"                    ROUND 2\n                 {self.robot2.name.upper()} vs {self.dinosaur2.name.upper()}\n")
        while self.battle_two == True:
            self.dinosaur2.attack(self.robot2.name)
            self.robot2.health = self.robot2.health - self.dinosaur2.attack_power
            if self.robot2.health > 0:
                print(f'Robot {self.robot2.name} has {self.robot2.health} health remaining!\n')
            if self.robot2.health <= 0:
                print(f"\nRobot {self.robot2.name} is killed!\n")
                break
            if self.dinosaur2.health > 0:
                self.robot2.attack(self.dinosaur2.name)
                self.dinosaur2.health = self.dinosaur2.health - self.robot2.active_weapon.attack_power
                if self.dinosaur2.health > 0:
                    print(f'Dino {self.dinosaur2.name} has {self.dinosaur2.health} health remaining!\n')
                if self.dinosaur2.health <= 0:
                    print(f"\nDino {self.dinosaur2.name} is killed!\n")
                    break

    def round_three(self):
        self.battle_three = True
        print(f"                    ROUND 3\n                 {self.robot3.name.upper()} vs {self.dinosaur3.name.upper()}\n")
        while self.battle_three == True:
            self.dinosaur3.attack(self.robot3.name)
            self.robot3.health = self.robot3.health - self.dinosaur3.attack_power
            if self.robot3.health > 0:
                print(f'Robot {self.robot3.name} has {self.robot3.health} health remaining!\n')
            if self.robot3.health <= 0:
                print(f"\nRobot {self.robot3.name} is killed!\n")
                break
            if self.dinosaur3.health > 0:
                self.robot3.attack(self.dinosaur3.name)
                self.dinosaur3.health = self.dinosaur3.health - self.robot3.active_weapon.attack_power
                if self.dinosaur3.health > 0:
                    print(f'Dino {self.dinosaur3.name} has {self.dinosaur3.health} health remaining!\n')
                if self.dinosaur3.health <= 0:
                    print(f"\nDino {self.dinosaur3.name} is killed!\n")
                    break

    def display_winner(self):
            if self.robot.health <= 0:
                print(f"Dino {self.dinosaur.name} wins!\n")
                print(f'It was an epic battle, which defined Robot {self.robot.name} as a looser... Oh, my bad. Defined him as DEAD Robot {self.robot.name}!\n')
            elif self.dinosaur.health <= 0:
                print(f"Robot {self.robot.name} wins! Nothing unpredictable.\n")
                print(f'Like I said, Dino {self.dinosaur.name} is an easy opponent for Robot {self.robot.name}. By the way, where is my winning bet?!\n')

    def fleet_herd_final_display(self):
        print("\nToday's battle was just a one of many in this EPIC WAR!\nThis war is far from the over!\n\nThanks for being with us!\n")
    
    def create_robot(self):
        self.robot = Robot(input("\nEnter Robot name: "), Weapon(("Knife"), 15))
        return self.robot

    def create_dinosaur(self):
        self.dinosaur = Dinosaur(input("Enter Dino name: "), 25)
        return self.dinosaur