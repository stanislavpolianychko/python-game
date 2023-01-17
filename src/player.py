import pygame


class Player:
    def __init__(self, size, coordinates, speed, color):
        self.width, self.height = size
        self.color = color
        self.speed = speed
        self.player_x, self.player_y = coordinates

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.player_x, self.player_y, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.player_x += self.speed
