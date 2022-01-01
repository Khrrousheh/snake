import pygame
from pygame.locals import *


def drwa_block():
    surface.fill((000, 255, 000))
    surface.blit(block, (block_x, block_y))
    pygame.display.update()


if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1080, 640))
    surface.fill((000, 255, 000))

    block = pygame.image.load('resources\wall (1).png').convert()
    block_x = 100
    block_y = 100
    surface.blit(block, (block_x, block_y))

    pygame.display.flip()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False

                if event.key == K_UP:
                    if block_y <= 0:
                        block_y = 640
                    block_y -= 16
                    print("up", block_y)
                    drwa_block()

                if event.key == K_DOWN:
                    if block_y >= 640:
                        block_y = 0
                    block_y += 16
                    print("down ", block_y)
                    drwa_block()

                if event.key == K_LEFT:
                    if block_x == 0:
                        block_x = 1080
                    block_x -= 16
                    print("left ", block_x)
                    drwa_block()

                if event.key == K_RIGHT:
                    if block_x >= 1080:
                        block_x = 0
                    block_x += 16
                    print("right", block_x)
                    drwa_block()

            elif event.type == QUIT:
                run = False
