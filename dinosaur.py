class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        print(f'{self.name} attacked {robot} and dealt {self.attack_power} of damage!')

