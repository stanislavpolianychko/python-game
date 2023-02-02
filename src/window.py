from configuration.config import config
from src.sections.game import game
from src.sections.ending import GameEnd
from src.sections.menu import Menu
from src.sections.loading import Loading

import pygame


class Window:
    """Class, to start main loop of the game."""
    def __init__(self):
        pygame.init()
        surface = pygame.display.set_mode((config.window['width'], config.window['height']))
        pygame.display.set_caption(config.window['label'])
        # pygame.display.set_icon(icon)

        self._game = game.Game(surface, config.game['background_image'])
        self._ending = GameEnd(surface, config.ending['background_image'])
        self._menu = Menu(surface, config.menu['background_image'])
        self._loading = Loading(surface, config.loading['background_image'])

    def run(self):
        while True:
            self._loading.run()
            self._menu.run()
            self._game.run()
            self._ending.run()
