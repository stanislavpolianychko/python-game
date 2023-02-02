import pygame
from src.sections.background import Background


class ScreenSection:
    # check if event is close game
    def __init__(self, surface, bg_image):
        self._surface = surface
        self._bg = Background(bg_image)
        self._clock = pygame.time.Clock()

    @staticmethod
    def _check_for_exit():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    # refresh all screen updates
    def _refresh(self):
        pygame.display.update()
        self._bg.set(self._surface)

