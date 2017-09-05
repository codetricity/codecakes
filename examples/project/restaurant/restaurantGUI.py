import sgc
from sgc.locals import *

import pygame
from pygame.locals import *


def findRestaurant():
    restaurantOn = True

pygame.init()
pygame.display.init()
pygame.font.init()

PURPLE = (199, 46, 245)
MINT = (193, 248, 230)

screen = sgc.surface.Screen((800, 600))

clock = pygame.time.Clock()

fontOhio = pygame.font.Font("fnt/ohio.ttf", 24)

btn = sgc.Button(label="Capitola",
                 label_font=fontOhio,
                 label_col=MINT,
                 col=PURPLE,
                 pos=(100, 100))

restaurantSurface = fontOhio.render("This is the text", True, (0, 0, 0))
restaurantOn = False

btn.on_click = findRestaurant

btn.add(0)

while True:
    time = clock.tick(30)

    for event in pygame.event.get():
        sgc.event(event)
        if event.type == QUIT:
            exit()
 
    screen.fill((0, 0, 0))
    sgc.update(time)
    if restaurantOn:
        screen.blit(restaurantSurface, (100, 400))
    pygame.display.flip()