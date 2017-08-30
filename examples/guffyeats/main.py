import pygame
import controller
import move

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)

guffy = pygame.image.load("assets/img/giraffe.png")
guffy_rect = pygame.Rect(300, 200, 64, 64)

direction = "stop"

gameon = True

while gameon:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameon = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            direction = controller.getDirection(direction)
    guffy_rect = move.onePixel(screen, direction, guffy_rect)
    screen.fill((0, 0, 0))
    screen.blit(guffy, guffy_rect)
    controller.blit(screen)
    pygame.display.update()
