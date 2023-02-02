from configuration.config import config
import random
import pygame


class Barrier:
    """Class of barrier, which initialise with
        random image, speed and coordinates"""
    def __init__(self):
        self._coord_x = random.randint(0, config.window['width'] - config.barrier['width'])
        self._coord_y = -config.barrier['height']
        self._speed = random.randint(config.barrier['min_speed'], config.barrier['max_speed'])

        self._image = self._init_type()

    # generate random image of barrier
    @staticmethod
    def _init_type():
        paths = (config.barrier['image1'], config.barrier['image2'], config.barrier['image3'])
        image_path = random.choice(paths)
        return pygame.image.load(image_path)

    # if barriers coordinates intersect other from list
    def has_free_coord(self, coordinates_list):
        self_x, self_y = self.coordinates
        for other_x, other_y in coordinates_list:
            left_up_x = other_x <= self_x <= other_x + config.barrier['width']
            left_up_y = other_y <= self_y <= other_y + config.barrier['height']

            left_down_x = left_up_x
            left_down_y = other_y <= self_y + config.barrier['height'] <= other_y + config.barrier['height']

            right_up_x = other_x <= self_x + config.barrier['width'] <= other_x + config.barrier['width']
            right_up_y = left_up_y

            right_down_x = right_up_x
            right_down_y = left_down_y

            if (left_up_x and left_up_y) or (left_down_x and left_down_y) or (right_up_x and right_up_y) \
                    or (right_down_x and right_down_y):
                return False
        return True

    # show barriers coordinates tuple
    @property
    def coordinates(self):
        return self._coord_x, self._coord_y

    # is barrier in window range
    @property
    def is_actual(self):
        if self._coord_y >= config.window['height']:
            return False
        return True

    # move barrier down
    def move_down(self):
        self._coord_y += self._speed

    # present barrier in window
    def draw(self, surface):
        surface.blit(self._image, self.coordinates)

