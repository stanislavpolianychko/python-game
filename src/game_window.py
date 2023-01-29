from configuration.config import config
import barriers_handler as bh
import background
import pygame
import player


class Window:
    """Class, to start main loop of the game."""
    def __init__(self, icon=None):
        # initialise pygame library
        pygame.init()
        self.__surface = pygame.display.set_mode((config.window['width'], config.window['height']))
        pygame.display.set_caption(config.window['label'])
        if icon:
            pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()

        # initialise all necessary instances
        self.__bg = background.Background()
        self.__player = player.Player()
        self.__barriers_handler = bh.BarriersHandler()

    # check if event is close game
    @staticmethod
    def __check_for_end():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    # refresh all screen updates
    def __refresh(self):
        pygame.display.update()
        self.__bg.set(self.__surface)

    # check if player haven't crashed on barrier
    def __review_win(self):
        if not self.__barriers_handler.barriers_coordinates_list:
            return True

        player_x, player_y = self.__player.coordinates
        for barrier_x, barrier_y in self.__barriers_handler.barriers_coordinates_list:
            left_top_x = barrier_x <= player_x <= barrier_x + config.barrier['width']
            left_top_y = barrier_y <= player_y <= barrier_y + config.barrier['height']

            right_top_x = barrier_x <= player_x + config.player['width'] <= barrier_x + config.barrier['width']
            right_top_y = barrier_y <= player_y <= barrier_y + config.barrier['height']

            if (left_top_x and left_top_y) or (right_top_x and right_top_y):
                return False
        return True

    # main loop of the game
    def start_game(self):
        while self.__review_win():
            self.__check_for_end()

            self.__player.move()
            self.__player.draw(self.__surface)

            self.__barriers_handler.update_barriers_list()
            self.__barriers_handler.move_barriers()
            self.__barriers_handler.present_barriers(self.__surface)

            self.__refresh()

            self.clock.tick(config.window['fps'])
