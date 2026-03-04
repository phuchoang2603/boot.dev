import random
import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(
            screen, "white", self.position, self.radius, LINE_WIDTH
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new1 = Asteroid(self.position.x, self.position.y, new_radius)
        new1.velocity = self.velocity.rotate(new_angle) * 1.2

        new2 = Asteroid(self.position.x, self.position.y, new_radius)
        new2.velocity = self.velocity.rotate(-new_angle) * 1.2
