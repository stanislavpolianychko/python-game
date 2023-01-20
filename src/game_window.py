import pygame
import player
import constants as const
import background


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

        # background image set
        self.bg = background.Background(const.BACK_GROUND_IMAGE_PATH)

        # player coordinates in win
        self.player = player.Player((const.PLAYER_X, const.PLAYER_Y), const.PLAYER_SPEED, const.PLAYER_IMAGE_PATH)

    # refresh all screen updates
    def refresh(self):
        pygame.display.update()
        self.bg.set_background(self.surface)

    # main loop of the window
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

