import pygame
from pygame import image
from pygame.locals import *
from Snake import SIZE, Snake
from Apple import Apple
import time


class Game:
    def __init__(self):
        self.speed = 0.3
        pygame.init()
        self.surface = pygame.display.set_mode((1080, 640))
        self.surface.fill((000, 255, 000))
        self.snake = Snake(self.surface, 6)
        self.apple = Apple(self.surface)
        self.snake.draw()
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2+SIZE:
            if y1 >= y2 and y1 <= y2+SIZE:
                self.apple.move()
                if self.speed != 0.0:
                    self.speed -= 0.02

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.is_collision(self.snake.block_x[0],
                          self.snake.block_y[0], self.apple.x, self.apple.y)

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

            self.play()
            time.sleep(self.speed)
