from configuration.config import config
from src.sections.game import game
from src.sections.ending import GameEnd

import pygame


class Window:
    """Class, to start main loop of the game."""
    def __init__(self):
        pygame.init()
        surface = pygame.display.set_mode((config.window['width'], config.window['height']))
        pygame.display.set_caption(config.window['label'])
        # pygame.display.set_icon(icon)

        self.game = game.Game(surface, config.game['background_image'])
        self.ending = GameEnd(surface, config.game['background_image'])

    def run(self):
        self.ending.run()
        self.game.run()