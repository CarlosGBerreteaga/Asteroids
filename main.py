import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():

    # Group Initialization
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # ensure Player sprites are added to our groups when constructed
    Player.containers = (updatable, drawable)

    # Asteroids group and container wiring
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)

    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()


    print("Starting Asteroids!")
    pygame.init()
    game_clock = pygame.time.Clock() 
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    exit_game = False

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    while not exit_game:
        screen.fill((0, 0, 0))  # Clear screen with black

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game Over!")
                exit_game = True
        
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()  # Update the full display Surface to the screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = game_clock.tick(60)/1000  # Cap the frame rate at 60 FPS

if __name__ == "__main__":
    main()
