import pygame
pygame.init()

while True:
    timer_number = pygame.time.get_ticks() / 1000.0
    timer_one_decimal = round(timer_number, 1)
    timer_string = str(timer_one_decimal)
    print(timer_string)
