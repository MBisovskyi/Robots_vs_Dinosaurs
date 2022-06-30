class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.choice_of_weapon()
        
    def choice_of_weapon(self):
        print("1. Cannon - damage 30        2. Blaster - damage 20      3. Sabre - damage 35")
        user_ipnut = int(input(f'Select a weapon: '))
        if user_ipnut == 1:
            self.name = "Cannon"
            self.attack_power = 30
        elif user_ipnut == 2:
            self.name = "Blaster"
            self.attack_power = 20
        elif user_ipnut == 3:
            self.name = "Sabre"
            self.attack_power = 35