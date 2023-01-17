import pygame
import player
import constants


class Window:
    def __init__(self, size, caption, icon=None):
        # initialise pygame library
        pygame.init()
        # create a surface (window) with defined size
        self.surface = pygame.display.set_mode(size)
        # set window params
        pygame.display.set_caption(caption)
        if icon:
            pygame.display.set_icon(icon)

        # player coordinates in win
        self.player = player.Player((10, 20), (size[0]//2, size[1]//2), 5, constants.COLOR_BLUE)

    def refresh(self):
        pygame.display.update()
        self.surface.fill(constants.COLOR_BLACK)

    def start_mainloop(self, fps):
        clock = pygame.time.Clock()

        while True:
            # check if event is close game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            # player movement
            self.player.move()
            self.player.draw(self.surface)

            self.refresh()

            # set a delay
            clock.tick(fps)

