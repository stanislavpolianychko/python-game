import pygame
from src.sections.screen_section import ScreenSection
"""in menu u can choose a diff lvl of game"""


class Menu(ScreenSection):
    def __init__(self, surface, bg_image):
        super().__init__(surface, bg_image)

    def run(self):
        pass
