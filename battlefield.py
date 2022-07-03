from logging import root
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
        self.herd = Herd()

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
        self.herd.create_herd()
        self.fleet_herd_battle()
        self.declaring_winner()

    def fleet_herd_battle(self):
        print(f"                Battle begins!\nAs robots had a chance to pick a weapon for themselves, I think it'll be fair enough if {self.herd.dinosaurs_list[0].name}, {self.herd.dinosaurs_list[1].name} and {self.herd.dinosaurs_list[2].name} attack first!\n")
        killed_robots_counter = 0
        killed_dinosaurs_counter = 0
        while self.battle == True:
            if self.herd.dinosaurs_list[0].health > 0:
                print(f'Dinosaur {self.herd.dinosaurs_list[0].name} attacked robot {self.fleet.robots_list[0].name}!')
                self.fleet.robots_list[0].health -= self.herd.dinosaurs_list[0].attack_power
                if self.fleet.robots_list[0].health <= 0:
                    killed_robots_counter += 1
                    print(f'\nThat was a final hit from dinosaur {self.herd.dinosaurs_list[0].name} that just killed robot {self.fleet.robots_list[0].name}. {self.fleet.robots_list[0].active_weapon.name} did not work this time!\n')
                    break
            if self.fleet.robots_list[0].health > 0:
                print(f'Robot {self.fleet.robots_list[0].name} attacked dino {self.herd.dinosaurs_list[0].name} with {self.fleet.robots_list[0].active_weapon.name}!')
                self.herd.dinosaurs_list[0].health -= self.fleet.robots_list[0].active_weapon.attack_power
                if self.herd.dinosaurs_list[0].health <= 0:
                    killed_dinosaurs_counter += 1
                    print(f"\nThe {self.fleet.robots_list[0].active_weapon.name} helped to robot {self.fleet.robots_list[0].name} to finish dino {self.herd.dinosaurs_list[0].name}!\n")
                    break
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        while killed_robots_counter > killed_dinosaurs_counter or killed_dinosaurs_counter > killed_robots_counter:
            if self.herd.dinosaurs_list[1].health > 0:
                print(f'Dinosaur {self.herd.dinosaurs_list[1].name} attacked robot {self.fleet.robots_list[1].name}!')
                self.fleet.robots_list[1].health -= self.herd.dinosaurs_list[1].attack_power
                if self.fleet.robots_list[1].health <= 0:
                    killed_robots_counter += 1
                    print(f'\nThat was a final hit from dinosaur {self.herd.dinosaurs_list[1].name} that just killed robot {self.fleet.robots_list[1].name}. {self.fleet.robots_list[1].active_weapon.name} did not work this time!\n')
                    break
            if self.fleet.robots_list[1].health > 0:
                print(f'Robot {self.fleet.robots_list[1].name} attacked dino {self.herd.dinosaurs_list[1].name} with {self.fleet.robots_list[1].active_weapon.name}!')
                self.herd.dinosaurs_list[1].health -= self.fleet.robots_list[0].active_weapon.attack_power
                if self.herd.dinosaurs_list[1].health <= 0:
                    killed_dinosaurs_counter += 1
                    print(f"\nThe {self.fleet.robots_list[1].active_weapon.name} helped to robot {self.fleet.robots_list[1].name} to finish dino {self.herd.dinosaurs_list[1].name}!\n")
                    break
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        while killed_robots_counter > killed_dinosaurs_counter or killed_dinosaurs_counter > killed_robots_counter or killed_robots_counter == killed_dinosaurs_counter:
            if self.herd.dinosaurs_list[2].health > 0:
                print(f'Dinosaur {self.herd.dinosaurs_list[2].name} attacked robot {self.fleet.robots_list[2].name}!')
                self.fleet.robots_list[2].health -= self.herd.dinosaurs_list[1].attack_power
                if self.fleet.robots_list[2].health <= 0:
                    killed_robots_counter += 1
                    print(f'\nThat was a final hit from dinosaur {self.herd.dinosaurs_list[2].name} that just killed robot {self.fleet.robots_list[2].name}. {self.fleet.robots_list[2].active_weapon.name} did not work this time!\n')
                    self.battle == True
                    break
            if self.fleet.robots_list[2].health > 0:
                print(f'Robot {self.fleet.robots_list[2].name} attacked dino {self.herd.dinosaurs_list[2].name} with {self.fleet.robots_list[2].active_weapon.name}!')
                self.herd.dinosaurs_list[2].health -= self.fleet.robots_list[0].active_weapon.attack_power
                if self.herd.dinosaurs_list[2].health <= 0:
                    killed_dinosaurs_counter += 1
                    print(f"\nThe {self.fleet.robots_list[2].active_weapon.name} helped to robot {self.fleet.robots_list[2].name} to finish dino {self.herd.dinosaurs_list[2].name}!\n")
                    self.battle == True
                    break
        print(f"Robots {killed_dinosaurs_counter} vs {killed_robots_counter} Dinosaurs\n")
        if killed_dinosaurs_counter > killed_robots_counter:
            self.winner = 'Robots'
        else:
            self.winner = 'Dinosaurs'
        return self.winner

    def declaring_winner(self):
        if self.winner == 'Robots':
            print(f'Today {self.winner} won a battle, but a war is not even over! Thanks for being with us today!\n')
        else:
            self.winner = 'Dinosaurs'
            print(f'Today {self.winner} won a battle, but a war is not even over! Thanks for being with us today!\n')