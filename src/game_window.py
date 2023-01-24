import random
import pygame
import player
import background
import barrier
from configuration.config import config


class Window:
    def __init__(self, size: (int, int), label: str, icon=None):
        # initialise pygame library
        pygame.init()
        # create a surface (window) with defined size
        self.surface = pygame.display.set_mode(size)
        # set window params
        pygame.display.set_caption(label)
        if icon:
            pygame.display.set_icon(icon)
        # background image set
        self.bg = background.Background(config.window['background_image'])
        # player coordinates in win
        player_coordinates = (config.player['start_x_coord'], config.player['start_y_coord'])
        self.player = player.Player(player_coordinates, config.player['speed'], config.player['image'])

    # refresh all screen updates
    def refresh(self):
        pygame.display.update()
        self.bg.set(self.surface)

    # main loop of the window
    def start_mainloop(self):
        clock = pygame.time.Clock()
        player_max_x = config.window['width'] - config.player['width']
        player_min_x = config.player['width']

        while True:
            self.check_for_end()

            # player movement
            self.player.move(player_min_x, player_max_x)
            self.player.draw(self.surface)
            self.refresh()

            # set a delay
            clock.tick(config.window['fps'])

    # check if event is close game
    @staticmethod
    def check_for_end():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
