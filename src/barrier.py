import random
import pygame


class Barrier:
    def __init__(self, image_path_list: list, image_width: int):
        self.bar_type = random.randint(0, 2)
        self.image = pygame.image.load([image_path_list[self.bar_type]])
        self.image_w = image_width
        self.position_x = 0
        self.speed = random.randint(5, 10)

    def fall_down(self):
        self.position_x += self.speed
