import pygame

pygame.init()
clock = pygame.time.Clock()

SIZE = (800, 600)
DISPLAY = pygame.display.set_mode(SIZE)
YELLOW = (255, 255, 128)
BLACK = (0, 0, 0)

timer_font = pygame.font.Font("font/animeace2_reg.ttf", 24)
start_time = pygame.time.get_ticks()

gameOn = True

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    
    DISPLAY.fill(BLACK)
    current_time = pygame.time.get_ticks() - start_time
    timer = current_time / 1000.0
    timer = "{0:.1f}".format(timer)
    timer_surface = timer_font.render("Time : " + str(timer), False, YELLOW)
    DISPLAY.blit(timer_surface, (0, 0))
    pygame.display.update()
