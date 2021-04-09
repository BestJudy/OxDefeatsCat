
#how to get started with a black box

import pygame
pygame.init()

win = pygame.display.set_mode((800, 800))

pygame.display.set_caption("Are you ready for your first game?")

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()