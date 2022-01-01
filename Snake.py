from pygame import surface
import pygame

SIZE = 40


class Snake:

    def __init__(self, parent_screen: surface, length: int) -> None:
        self.length = length
        self.surface = parent_screen
        self.block = pygame.image.load('resources\dot.png').convert()
        self.block_x = [SIZE]*length
        self.block_y = [SIZE]*length
        self.direction = 'down'

    def draw(self):
        self.surface.fill((000, 255, 000))
        for i in range(0, self.length):
            self.surface.blit(self.block, (self.block_x[i], self.block_y[i]))
        pygame.display.update()

    def move_Left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length-1, 0, -1):
            self.block_x[i] = self.block_x[i-1]
            self.block_y[i] = self.block_y[i-1]

        if self.direction == 'down':
            if self.block_y[0] >= 640:
                self.block_y[0] = 0
            self.block_y[0] += SIZE

        elif self.direction == 'up':
            if self.block_y[0] <= 0:
                self.block_y[0] = 640
            self.block_y[0] -= SIZE

        elif self.direction == 'left':
            if self.block_x[0] <= 0:
                self.block_x[0] = 1080
            self.block_x[0] -= SIZE

        elif self.direction == 'right':
            if self.block_x[0] >= 1080:
                self.block_x[0] = 0
            self.block_x[0] += SIZE

        self.draw()
