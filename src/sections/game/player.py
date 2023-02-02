from configuration.config import config
import pygame


class Player:
    """Class of player instance."""
    def __init__(self):
        self._speed = config.player['speed']
        self._image = pygame.image.load(config.player['image'])
        self._player_x = config.player['start_x_coord']
        self._player_y = config.player['start_y_coord']

    @property
    def coordinates(self):
        return self._player_x, self._player_y

    # player movement
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self._player_x >= config.player['min_x_coord']:
            self._player_x -= self._speed
        elif keys[pygame.K_RIGHT] and self._player_x <= config.player['max_x_coord']:
            self._player_x += self._speed

    # draw player in defined surface
    def draw(self, surface):
        surface.blit(self._image, self.coordinates)
