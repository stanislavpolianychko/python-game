import pygame


class Player:
    def __init__(self, coordinates, speed, image_path):
        # initialise player params
        self.speed = speed
        self.image = pygame.image.load(image_path)
        self.player_x, self.player_y = coordinates

    # draw player in defined surface
    def draw(self, surface):
        surface.blit(self.image, (self.player_x, self.player_y))

    # player movement
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.player_x += self.speed
