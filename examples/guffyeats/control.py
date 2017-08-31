import pygame
import os


class Arrows:
    def __init__(self):

        current_dir = os.getcwd().split("/")[-1]
        arrows_dir = "assets/img/arrows/"
        if current_dir == "examples":
            arrows_dir = "guffyeats/" + arrows_dir

        self.up = pygame.image.load(arrows_dir + "up.png")
        self.up_rect = pygame.Rect(610, 300, 55, 100)

        self.down_rect = pygame.Rect(610, 475, 55, 100)
        self.down = pygame.image.load(arrows_dir + "down.png")

        self.left = pygame.image.load(arrows_dir + 'left.png')
        self.left_rect = pygame.Rect(500, 400, 100, 55)

        self.right = pygame.image.load(arrows_dir + 'right.png')
        self.right_rect = pygame.Rect(680, 400, 100, 55)

    def blit(self, screen):
        screen.blit(self.up, self.up_rect)
        screen.blit(self.down, self.down_rect)
        screen.blit(self.left, self.left_rect)
        screen.blit(self.right, self.right_rect)

    def getDirection(self, direction, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.up_rect.collidepoint(mouse_pos):
                    direction = "up"
                elif self.down_rect.collidepoint(mouse_pos):
                    direction = "down"
                elif self.right_rect.collidepoint(mouse_pos):
                    direction = "right"
                elif self.left_rect.collidepoint(mouse_pos):
                    direction = "left"
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_RIGHT, pygame.K_d]:
                    direction = "right"
                elif event.key in [pygame.K_LEFT, pygame.K_a]:
                    direction = "left"
                elif event.key in [pygame.K_UP, pygame.K_w]:
                    direction = "up"
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    direction = "down"            
        return direction
