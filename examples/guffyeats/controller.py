import pygame


up = pygame.image.load("assets/img/arrows/up.png")
up_rect = pygame.Rect(610, 300, 55, 100)

down_rect = pygame.Rect(610, 475, 55, 100)
down = pygame.image.load("assets/img/arrows/down.png")

left = pygame.image.load('assets/img/arrows/left.png')
left_rect = pygame.Rect(500, 400, 100, 55)

right = pygame.image.load('assets/img/arrows/right.png')
right_rect = pygame.Rect(680, 400, 100, 55)


def blit(screen):
    screen.blit(up, up_rect)
    screen.blit(down, down_rect)
    screen.blit(left, left_rect)
    screen.blit(right, right_rect)


def getDirection(direction):
    mouse_pos = pygame.mouse.get_pos()

    if up_rect.collidepoint(mouse_pos):
        direction = "up"
    elif down_rect.collidepoint(mouse_pos):
        direction = "down"
    elif right_rect.collidepoint(mouse_pos):
        direction = "right"
    elif left_rect.collidepoint(mouse_pos):
        direction = "left"
    return direction
