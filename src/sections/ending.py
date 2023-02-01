import pygame
from src.sections.screen_section import ScreenSection


class GameEnd(ScreenSection):
    def __init__(self, surface, bg_image):
        super().__init__(surface, bg_image)

    @staticmethod
    def _is_space_pressed():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return True
        return False

    def run(self):
        while True:
            if self._is_space_pressed():
                break
            self._check_for_exit()
            self._refresh()
