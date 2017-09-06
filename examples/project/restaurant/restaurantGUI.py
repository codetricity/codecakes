import sgc
from sgc.locals import *

import pygame
from pygame.locals import *
import random


class RestaurantButton(sgc.Button):
    def gameInit(self):
        self.on = False
        
    def on_click(self):
        self.message = ""
        self.on = True

def randomRestaurant():
    restaurants = [
        "Sushi Garden",
        "Asian Express",
        "Mayflower",
        "Betty's Burgers",
        "Erik's Deli Cafe",
        "Avenue Cafe",
        "Dharma's",
        "Wasabi Tapas",
        "Roux Dat Cajun",
        "Paradise Beach Grille",
        "Taqueria Vallata",
        "iCrave",
        "Chipotle",
        "East Side Eatery"
    ]
    randRestaurant = random.choice(restaurants)
    return randRestaurant


pygame.init()
pygame.display.init()
pygame.font.init()

PURPLE = (199, 46, 245)
MINT = (193, 248, 230)

screen = sgc.surface.Screen((800, 600))

clock = pygame.time.Clock()

fontOhio = pygame.font.Font("fnt/ohio.ttf", 30)
fontAbove = pygame.font.Font("fnt/above.ttf", 20)
fontLarge = pygame.font.Font("fnt/ohio.ttf", 52)
fontTitle = pygame.font.Font("fnt/painter.ttf", 84)

btn = RestaurantButton(label="Capitola",
                       label_font=fontAbove,
                       label_col=MINT,
                       col=PURPLE,
                       pos=(100, 150))

btn.gameInit()

label = sgc.Label(pos=(20, 240),
                  col=(255, 255, 255),
                  text="",
                  font=fontLarge)

mealChooser = sgc.Combo(
                    pos=(400, 150),
                    label="Meal",
                    label_side="top",
                    values=("breakfast", "lunch", "dinner", "snack"),
                    selection=1)

titleSurface = fontTitle.render("Caitlyn's> Restaurants", True, PURPLE)

btn.add(0)
label.add(1)
mealChooser.add(2)

while True:
    time = clock.tick(30)

    for event in pygame.event.get():
        sgc.event(event)
        if event.type == pygame.QUIT:
            exit()
 
    sgc.update(time)
    if btn.on:
        selection = mealChooser.selection
        meals = {0: "breakfast", 1: "lunch", 2: "dinner", 3: "snack"}
        label.text = (
                "Caitlyn recommends " + randomRestaurant() +
                " for " + meals[selection])
        btn.on = False
 
    screen.fill((0, 0, 0))
    screen.blit(titleSurface, (10, 10))
    sgc.update(time)
    pygame.display.flip()