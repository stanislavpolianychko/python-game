from configuration.config import config
import pygame


class Player:
    def __init__(self):
        self.__speed = config.player['speed']
        self.__image = pygame.image.load(config.player['image'])
        self.__player_x = config.player['start_x_coord']
        self.__player_y = config.player['start_y_coord']

    @property
    def coordinates(self):
        return self.__player_x, self.__player_y

    # player movement
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.__player_x >= config.player['min_x_coord']:
            self.__player_x -= self.__speed
        elif keys[pygame.K_RIGHT] and self.__player_x <= config.player['max_x_coord']:
            self.__player_x += self.__speed

    # draw player in defined surface
    def draw(self, surface):
        surface.blit(self.__image, self.coordinates)
