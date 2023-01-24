import pygame


class Background:
    def __init__(self, image_path):
        self.bg_image = pygame.image.load(image_path)

    def set(self, surface):
        surface.blit(self.bg_image, (0, 0))
