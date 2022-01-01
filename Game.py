import pygame
from pygame.locals import *
from Snake import Snake
import time


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1080, 640))
        self.surface.fill((000, 255, 000))
        self.snake = Snake(self.surface, 2)
        self.snake.draw()

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_Left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    run = False

            self.snake.walk()
            time.sleep(0.2)
