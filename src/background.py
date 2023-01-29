from configuration.config import config
import pygame


class Background:
    """Class to init background image and display it"""
    def __init__(self):
        self.__bg_image = pygame.image.load(config.window['background_image'])

    # set background image
    def set(self, surface):
        surface.blit(self.__bg_image, (0, 0))