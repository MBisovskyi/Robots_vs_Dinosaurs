class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        print(f'Dinosaur {self.name} attacked Robot {robot} and dealt {self.attack_power} of damage!')


