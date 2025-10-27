from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius, SHOT_COLOR, speed_x, speed_y):
        super().__init__(x, y, radius)
        self.color = SHOT_COLOR
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self, dt):
        self.position.x += self.speed_x * dt
        self.position.y += self.speed_y * dt

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)