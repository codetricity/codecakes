import pygame
import controller

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode((size))

controller.blit(screen)
direction = "stop"

gameon = True

while gameon:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            direction = controller.getDirection(direction)
    print(direction)
    pygame.display.update()
