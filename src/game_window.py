import random
import pygame
import player
import constants as const
import background
import field_column
import barrier


class Window:
    columns = [field_column.Column(num) for num in range(0, const.COLUMNS_COUNT-1)]

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
        self.bg = background.Background(const.BACK_GROUND_IMAGE_PATH)

        # player coordinates in win
        self.player = player.Player((const.PLAYER_X, const.PLAYER_Y), const.PLAYER_SPEED, const.PLAYER_IMAGE_PATH)

        # initialise columns and barriers inside
        self.init_columns()

    # refresh all screen updates
    def refresh(self):
        pygame.display.update()
        self.bg.set_background(self.surface)

    # main loop of the window
    def start_mainloop(self, fps: int):
        clock = pygame.time.Clock()

        while True:
            self.check_for_end()

            self.move_barriers()
            self.present_columns()

            # player movement
            self.player.move(const.MIN_X, const.MAX_X)
            self.player.draw(self.surface)
            self.refresh()

            # set a delay
            clock.tick(fps)

    # initialise columns list
    def init_columns(self):
        for column in self.columns:
            if random.randint(0, 2) == 1:
                column.set_barrier(barrier.Barrier())
                column.barrier.init_type(const.BARRIERS_LIST, const.BARRIERS_WIDTH)

    # method moves every barrier down with defined speed
    def move_barriers(self):
        for column in self.columns:
            if not column.is_free:
                column.barrier.fall_down()

    # method present every barrier in defined coordinates
    def present_columns(self):
        for column in self.columns:
            if not column.is_free:
                column.draw_barrier(self.surface)

    # check if event is close game
    @staticmethod
    def check_for_end():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
