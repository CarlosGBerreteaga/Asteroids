from constants import ASTEROID_KINDS, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_SPAWN_RATE
from circleshape import CircleShape
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        # pygame.draw.circle(surface, color, center, radius, width)
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "white", center, int(self.radius), 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_radius = self.radius
        old_velocity_vector = self.velocity
        old_position_x = self.position.x
        old_position_y = self.position.y
        old_container = self.containers
        self.kill() # Remove the current asteroid
        if old_radius< ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        new_velocity_vector1 = old_velocity_vector.rotate(random_angle)
        new_velocity_vector2 = old_velocity_vector.rotate(-random_angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(old_position_x, old_position_y, new_radius)
        asteroid1.velocity = new_velocity_vector1
        asteroid1.add(old_container)  # Add to the same groups as the original asteroid
        
        asteroid2 = Asteroid(old_position_x, old_position_y, new_radius)
        asteroid2.velocity = new_velocity_vector2
        asteroid2.add(old_container)  # Add to the same groups as the original asteroid
        


        