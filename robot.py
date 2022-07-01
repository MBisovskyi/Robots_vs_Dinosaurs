from weapon import Weapon

class Robot:
    def __init__(self, name, active_weapon):
        self.name = name
        self.health = 100
        self.active_weapon = active_weapon
    
    def attack(self, dinosaur):
        print(f'Robot {self.name} attacked Dino {dinosaur.name} with {self.active_weapon.name}!')
    
    def choose_weapon(self, dinosaur):
        print(f"                    Available weapon for Robot {self.name}\n")
        print("1. Cannon        2. Blaster      3. Sabre\n")
        user_ipnut = int(input(f'Select a weapon: '))
        if user_ipnut == 1:
            self.active_weapon = Weapon('Cannon', 30)
        elif user_ipnut == 2:
            self.active_weapon = Weapon('Blaster', 20)
        elif user_ipnut == 3:
            self.active_weapon = Weapon('Sabre', 35)
            return self.active_weapon
        print()