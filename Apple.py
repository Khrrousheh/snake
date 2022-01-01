import pygame
import random
from pygame import surface

SIZE = 40


class Apple:
    def __init__(self, parent_suface: surface) -> None:
        self.item = pygame.image.load("resources\wall.png").convert()
        self.surface = parent_suface
        self.x = SIZE*2
        self.y = SIZE*5

    def draw(self):
        self.surface.blit(self.item, (self.x, self.y))
        pygame.display.update()

    def move(self):
        self.x = random.randint(0, 27)*SIZE
        self.y = random.randint(0, 16)*SIZE
        self.draw()
