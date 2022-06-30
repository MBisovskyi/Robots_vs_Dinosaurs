from dinosaur import Dinosaur
from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Cannon', 30)
    
    def attack(self, dinosaur):
        print(f'Robot {self.name} attacked Dinosaur {dinosaur} and dealt {self.active_weapon.attack_power} of damage!')


        
        

