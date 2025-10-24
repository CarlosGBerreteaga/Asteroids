import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    exit_game = False

    while not exit_game:
        screen.fill((0, 0, 0))  # Clear screen with black
        pygame.display.flip()  # Update the full display Surface to the screen


if __name__ == "__main__":
    main()
