from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        pass

    def run_games(self):
        pass

    def display_welcome(self):
        pass
    
    def battle_phase(self):
        pass

    def display_winner(self):
        pass

dinosaur = Dinosaur('Arghhh', 25)
robot = Robot('TasteOfSteel')
dinosaur.attack(robot.name)
robot.attack(dinosaur.name)
