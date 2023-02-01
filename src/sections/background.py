import pygame


class Background:
    """Class to init background image and display it"""

    def __init__(self, image_path):
        self.__bg_image = pygame.image.load(image_path)

    # set background image
    def set(self, surface):
        surface.blit(self.__bg_image, (0, 0))
