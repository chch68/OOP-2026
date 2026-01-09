import pygame   
class Game:
    def __init__(self):
        pygame.init()
        print('Welcome to the Game!')
class Player:
    def __init__(self, name):
        self.name = name
        print(f'Player {self.name} has entered the game.')