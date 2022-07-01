from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Cannon', 30)
    
    def attack(self, dinosaur):
        print(f"                    Available weapon for Robot {self.name}\n")
        print("1. Cannon - damage 30        2. Blaster - damage 20      3. Sabre - damage 35")
        print(" ")
        user_ipnut = int(input(f'Select a weapon: '))
        if user_ipnut == 1:
            self.active_weapon = cannon
        elif user_ipnut == 2:
            self.active_weapon = blaster
        elif user_ipnut == 3:
            self.active_weapon = sabre
        print(" ")
        print(f'Robot {self.name} attacked Dinosaur {dinosaur} with a {self.active_weapon.name} and dealt {self.active_weapon.attack_power} of damage!') 
        
cannon = Weapon('Cannon', 30)
blaster = Weapon('Blaster', 20)
sabre = Weapon('Sabre', 35)