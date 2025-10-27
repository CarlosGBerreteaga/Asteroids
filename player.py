from constants import *
from circleshape import CircleShape
from shot import Shot
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        try:
            points = self.triangle()
            print("Points:", points)  # This will help us see the values
            pygame.draw.polygon(screen, "white", points, 2)
        except Exception as e:
            print("Error drawing:", e)  # This will show us any error that occurs

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)  # Negative dt for left rotation
        if keys[pygame.K_d]:
            self.rotate(dt)   # Positive dt for right rotation
        if keys[pygame.K_w]:
            self.move(dt)     # Position dt for forward direction
        if keys[pygame.K_s]:
            self.move(-dt)    # Negative dt for backward direction
        if keys[pygame.K_SPACE]:
             return self.shot() 
    
    def shot(self):
        direction = pygame.Vector2(0,1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, SHOT_COLOR, 
                   direction.x * SHOT_SPEED, direction.y * SHOT_SPEED)
        return shot
