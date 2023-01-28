from configuration.config import config
import random
import pygame


class Barrier:
    def __init__(self):
        self.__coord_x = random.randint(0, config.window['width'] - config.barrier['width'])
        self.__coord_y = 0

        self.__image = self.__init_type()

    @property
    def coordinates(self):
        return self.__coord_x, self.__coord_y

    @property
    def is_actual(self):
        if self.__coord_y >= config.window['height'] - config.barrier['height']:
            return False
        return True

    def __init_type(self):
        if self.__image:
            return
        paths = (config.barrier['image1'], config.barrier['image2'], config.barrier['image3'], config.barrier['image4'])
        image_path = random.choice(paths)
        return pygame.image.load(image_path)

    def move_down(self):
        self.__coord_y += config.barrier['speed']
