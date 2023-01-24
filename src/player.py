import pygame


class Player:
    def __init__(self, coordinates: (int, int), speed: int, image_path: str):
        self.speed = speed
        self.image = pygame.image.load(image_path)
        self.player_x, self.player_y = coordinates

    # player movement
    def move(self, min_x: int, max_x: int):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.player_x >= min_x:
            self.player_x -= self.speed
        elif keys[pygame.K_RIGHT] and self.player_x <= max_x:
            self.player_x += self.speed

    # draw player in defined surface
    def draw(self, surface):
        surface.blit(self.image, (self.player_x, self.player_y))
