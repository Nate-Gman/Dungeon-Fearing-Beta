import pygame

class Realm():
    def __init__(self):
        self.gameSprites = pygame.sprite.Group()
        self.Walls = pygame.sprite.Group()
        self.Fountains = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.allies = pygame.sprite.Group()