import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while 1 == 0:
        screen.fill(000)
        pygame.display.flip()

if __name__ == "__main__":
    main()