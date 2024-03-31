import pygame.display
from triangle import Triangle
from square import Square
from settings import *


class Game:

    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.triangle = Triangle()
        self.square = Square()
        self.bounce_sound = pygame.mixer.Sound('sfx/pop.wav')
        self.bounce_sound.set_volume(.1)
        self.display_surface.fill(BG_COLOR)
        self.triangle.draw(self.display_surface)

    def check_collisions(self):

        right_line_collision = self.square.rect.clipline(self.triangle.right_corner, self.triangle.bottom_corner)
        left_line_collision = self.square.rect.clipline(self.triangle.left_corner, self.triangle.bottom_corner)
        top_line_collision = self.square.rect.clipline(self.triangle.left_corner, self.triangle.right_corner)
        if right_line_collision:
            vector_x = self.triangle.bottom_corner[0] - self.triangle.right_corner[0]
            vector_y = self.triangle.bottom_corner[1] - self.triangle.right_corner[1]
            line_vector = pygame.math.Vector2(vector_x, vector_y)
            angle = self.square.velocity.angle_to(line_vector)

            if angle > 90:
                impact_corner = right_line_collision[1]
                increment = self.square.rect.bottom - impact_corner[1]
                self.square.rect.bottomright = (impact_corner[0], impact_corner[1] - increment)
            else:
                impact_corner = right_line_collision[0]
                increment = self.square.rect.right - impact_corner[0]
                self.square.rect.bottomright = (impact_corner[0] - increment, impact_corner[1])

            rotated_vector = self.square.velocity.rotate(2 * angle)
            new_vel = 1.01 * rotated_vector.length()
            rotated_vector.scale_to_length(new_vel)
            self.square.velocity = rotated_vector
            self.bounce_sound.play()

        elif left_line_collision:
            vector_x = self.triangle.bottom_corner[0] - self.triangle.left_corner[0]
            vector_y = self.triangle.bottom_corner[1] - self.triangle.left_corner[1]
            line_vector = pygame.math.Vector2(vector_x, vector_y)
            angle = self.square.velocity.angle_to(line_vector)

            if angle < 90:
                impact_corner = left_line_collision[1]
                increment = self.square.rect.bottom - impact_corner[1]
                self.square.rect.bottomleft = (impact_corner[0], impact_corner[1] - increment)
            else:
                impact_corner = left_line_collision[0]
                increment = self.square.rect.left - impact_corner[0]
                self.square.rect.bottomleft = (impact_corner[0] - increment, impact_corner[1])

            rotated_vector = self.square.velocity.rotate(2 * angle)
            new_vel = 1.01 * rotated_vector.length()
            rotated_vector.scale_to_length(new_vel)
            self.square.velocity = rotated_vector
            self.bounce_sound.play()

        elif top_line_collision:
            vector_x = self.triangle.left_corner[0] - self.triangle.right_corner[0]
            vector_y = self.triangle.left_corner[1] - self.triangle.right_corner[1]
            line_vector = pygame.math.Vector2(vector_x, vector_y)
            angle = self.square.velocity.angle_to(line_vector)

            impact_y = top_line_collision[0][1]
            increment = impact_y - self.square.rect.top
            self.square.rect.top = impact_y + increment

            rotated_vector = self.square.velocity.rotate(2 * angle)
            new_vel = 1.01 * rotated_vector.length()
            rotated_vector.scale_to_length(new_vel)
            self.square.velocity = rotated_vector
            self.bounce_sound.play()

    def run(self, dt, start):

        if start:
            self.square.update(dt)
            self.check_collisions()
        self.square.draw(self.display_surface)

        pygame.display.flip()
