import pygame

SIZE = (800, 600)

DISPLAY = pygame.display.set_mode(SIZE)

cupcake = pygame.image.load("img/cupcake.png")

gameOn = True

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    pygame.display.update()
