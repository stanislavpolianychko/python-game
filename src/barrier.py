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
        if self.__coord_y >= config.window['height']:
            return False
        return True

    @staticmethod
    def __init_type():
        paths = (config.barrier['image1'], config.barrier['image2'], config.barrier['image3'], config.barrier['image4'])
        image_path = random.choice(paths)
        return pygame.image.load(image_path)

    def has_free_coord(self, coordinates_list):
        self_x, self_y = self.coordinates
        for other_x, other_y in coordinates_list:
            left_up_x = other_x <= self_x <= other_x + config.barrier['width']
            left_up_y = other_y <= self_y <= other_y + config.barrier['height']

            left_down_x = other_x <= self_x <= other_x + config.barrier['width']
            left_down_y = other_y <= self_y + config.barrier['height'] <= other_y + config.barrier['height']

            right_up_x = other_x <= self_x + config.barrier['width'] <= other_x + config.barrier['width']
            right_up_y = other_y <= self_y <= other_y + config.barrier['height']

            right_down_x = other_x <= self_x + config.barrier['width'] <= other_x + config.barrier['width']
            right_down_y = other_y <= self_y + config.barrier['height'] <= other_y + config.barrier['height']

            if (left_up_x and left_up_y) or (left_down_x and left_down_y) or (right_up_x and right_up_y) \
                    or (right_down_x and right_down_y):
                return False
        return True

    def move_down(self):
        self.__coord_y += config.barrier['speed']

    def draw(self, surface):
        surface.blit(self.__image, self.coordinates)

