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
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            gameon = False
        
    direction = controller.getDirection(direction, event_list)
    guffy_rect = move.onePixel(screen, direction, guffy_rect)
    screen.fill((0, 0, 0))
    screen.blit(guffy, guffy_rect)
    controller.blit(screen)
    pygame.display.update()
