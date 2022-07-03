from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs_list = []

    def create_herd(self):
        self.create_dinosaur()

    def create_dinosaur(self):
        dinosaurs_counter = 0
        while dinosaurs_counter != 3:
            self.dinosaur = Dinosaur(input("Enter dinosaur name: "), 22)
            self.dinosaurs_list.append(self.dinosaur)
            dinosaurs_counter += 1
            if dinosaurs_counter == 1:
                print(f"What a monster here! It's name is {self.dinosaur.name}!\n")
            elif dinosaurs_counter == 2:
                print(f"Look at this guy! I think that {self.dinosaur.name} can smash them all!\n")
            elif dinosaurs_counter == 3:
                print(f"The last one is {self.dinosaur.name}! It's name sounds familiar...\n")