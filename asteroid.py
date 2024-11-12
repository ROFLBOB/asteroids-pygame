import pygame
import constants
import random
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            self.kill()
            return
        #split into 2 new asteroids
        random_angle = random.uniform(20.0, 50.0)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        first_velocity = pygame.Vector2(self.velocity).rotate(random_angle)
        second_velocity = pygame.Vector2(self.velocity).rotate(-random_angle)
        first_split = Asteroid(self.position.x, self.position.y, new_radius)
        second_split = Asteroid(self.position.x, self.position.y, new_radius)
        first_split.velocity = first_velocity * 1.2
        second_split.velocity = second_velocity
        for group in self.groups():
            group.add(first_split)
            group.add(second_split)
        self.kill()

        