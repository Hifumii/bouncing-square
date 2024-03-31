import pygame.draw

from settings import *
from math import sqrt


class Triangle:

    def __init__(self):
        self.side = TRIANGLE_SIDE
        self.height = round((self.side * sqrt(3)) / 2)
        self.color = TRIANGLE_COLOR
        self.width = 3
        self.center = (round(WINDOW_WIDTH / 2), round(WINDOW_HEIGHT / 2))
        self.left_corner = (self.center[0] - self.side / 2, self.center[1] - self.height / 2)
        self.right_corner = (self.center[0] + self.side / 2, self.center[1] - self.height / 2)
        self.bottom_corner = (self.center[0], self.center[1] + self.height / 2)

    def draw(self, surface):
        pygame.draw.lines(surface, self.color, True, [self.left_corner, self.right_corner, self.bottom_corner],
                          self.width)
