import pygame
from settings import *
from color import ColorChanger


class Square:

    def __init__(self):
        self.width = SQUARE_SIDE
        self.height = SQUARE_SIDE
        self.x = (WINDOW_WIDTH - self.width) / 2 - 55
        self.y = (WINDOW_HEIGHT - self.height) / 2 - 100
        self.rect = pygame.rect.Rect((self.x, self.y), (self.width, self.height))

        self.color = SQUARE_COLOR
        self.outline_color = SQUARE_OUTLINE_COLOR
        self.color_changer = ColorChanger()

        self.gravity = 500
        self.velocity = pygame.math.Vector2(0, 0)

    def move(self, dt):
        self.apply_gravity(dt)
        self.rect.x += self.velocity[0] * dt
        self.rect.y += self.velocity[1] * dt

    def apply_gravity(self, dt):
        self.velocity[1] += self.gravity * dt

    def update(self, dt):
        self.move(dt)
        self.color = self.color_changer.change_color()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, self.outline_color, self.rect, 1)
        # pygame.draw.circle(surface, self.color, self.rect.center, self.width/2)
        # pygame.draw.circle(surface, self.outline_color, self.rect.center, self.width / 2, 1)
