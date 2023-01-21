import random
import pygame


class Barrier:
    def __init__(self):
        self.image = None
        self.image_w = 64
        self.bar_type = None
        self.position = 0
        self.falling_speed = random.randint(5, 10)

    def init_type(self, images_list: list, image_width: int):
        self.bar_type = random.randint(0, 2)
        self.image = pygame.image.load([images_list[self.bar_type]])
        self.image_w = image_width

    def fall_down(self):
        self.position -= self.falling_speed
