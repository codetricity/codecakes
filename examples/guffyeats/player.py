import pygame
import os


class Guffy:
    def __init__(self):
        current_dir = os.getcwd().split("/")[-1]
        image_dir = "assets/img/"
        if current_dir == "examples":
            image_dir = "guffyeats/" + image_dir
        self.image = pygame.image.load(image_dir + 'giraffe.png')
        self.rect = pygame.Rect(300, 200, 64, 64)