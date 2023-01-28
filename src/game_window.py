from configuration.config import config
import pygame
import player
import background
import barriers_handler


class Window:
    def __init__(self, icon=None):
        # initialise pygame library
        pygame.init()
        self.__surface = pygame.display.set_mode((config.window['width'], config.window['height']))
        pygame.display.set_caption(config.window['label'])
        if icon:
            pygame.display.set_icon(icon)

        # background image instance
        self.__bg = background.Background()
        # player instance
        self.__player = player.Player()
        # list with all barriers instances
        self.__barriers_handler = barriers_handler.BarriersHandler()

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

    # main loop of the window
    def start_mainloop(self):
        clock = pygame.time.Clock()

        while True:
            self.__check_for_end()

            self.__player.move()
            self.__player.draw(self.__surface)
            self.__refresh()

            # set a delay
            clock.tick(config.window['fps'])
