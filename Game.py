import pygame
from pygame import image
from pygame.locals import *
from Snake import SIZE, Snake
from Apple import Apple
import time


class Game:
    def __init__(self):
        self.speed = float(0.2)
        pygame.init()
        self.surface = pygame.display.set_mode((1080, 640))
        self.surface.fill((000, 255, 000))
        self.running = True
        self.snake = Snake(self.surface, 2)
        self.apple = Apple(self.surface)
        self.snake.draw()
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2+SIZE:
            if y1 >= y2 and y1 <= y2+SIZE:
                return True
        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()

        if self.is_collision(self.snake.block_x[0], self.snake.block_y[0], self.apple.x, self.apple.y):
            self.apple.move()
            self.snake.increase_length()
            if(self.speed >= float(0.1)):
                self.speed -= float(0.02)

        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.block_x[0], self.snake.block_y[0], self.snake.block_x[i], self.snake.block_y[i]):
                raise "Game Over"

        self.display_score()
        self.display_speed()
        pygame.display.flip()

    def display_speed(self):
        font = pygame.font.SysFont('arial', 30)
        mySpeed = font.render(f'Speed: {self.speed}', True, (255, 0, 200))
        self.surface.blit(mySpeed, (0, 10))

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(
            f'Score: {self.snake.length}', True, (255, 0, 200))
        self.surface.blit(score, (800, 10))

    def run(self):

        while self.running:
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

            try:
                self.play()
            except Exception as e:
                self.running = False
            time.sleep(self.speed)
        else:
            print('gameOver')
