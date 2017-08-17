import pygame

pygame.init()

clock = pygame.time.Clock()

SIZE = (800, 600)

DISPLAY = pygame.display.set_mode(SIZE)

start_time = pygame.time.get_ticks()

gameOn = True

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    current_time = pygame.time.get_ticks() - start_time
    timer = current_time / 1000.0
    print(timer)
    pygame.display.update()
