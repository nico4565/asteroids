from constants import *
import pygame
from circleshape import *
import random

class Asteroid(Circleshape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        positive_rot_velocity =self.velocity.rotate(random_angle)
        negative_rot_velocity =self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_pos = Asteroid(self.position.x, self.position.y,new_radius)
        asteroid_pos.velocity = positive_rot_velocity*1.2
        asteroid_neg = Asteroid(self.position.x, self.position.y,new_radius)
        asteroid_neg.velocity = negative_rot_velocity*1.2