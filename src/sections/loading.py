from configuration.config import config
from time import sleep
from src.sections.screen_section import ScreenSection
import pygame
"""loading class, which ran loading of the game animation"""


class Loading(ScreenSection):
    def __init__(self, surface, bg_image):
        super().__init__(surface, bg_image)
        self.start_x, self.start_y = (0, 0)
        self.current_x, self.current_y = (0, 0)
        self.end_x, self.end_y = (300, 100)

    def do_step(self):
        pygame.draw.rect(self._surface,
                         tuple(map(int, config.loading['animation color'].split())),
                         pygame.Rect(30, 30, 60, 60)
                         )

    def run(self):
        while True:
            self._check_for_exit()
            sleep(1)
            self._refresh()
            self._clock.tick(config.window['fps'])
