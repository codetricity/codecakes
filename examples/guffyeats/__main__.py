import pygame
import control
import move
import player


def main():

    pygame.init()

    size = (800, 600)
    screen = pygame.display.set_mode(size)

    controller = control.Arrows()
    guffy = player.Guffy()

    direction = "stop"

    gameon = True

    while gameon:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                gameon = False
            
        direction = controller.getDirection(direction, event_list)
        guffy.rect = move.onePixel(screen, direction, guffy.rect)
        screen.fill((0, 0, 0))
        screen.blit(guffy.image, guffy.rect)
        controller.blit(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
