import pygame
from pygame.math import Vector2 as vec

from consts import DEBUG, WIDTH


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[float, float], length=WIDTH / 4, width=20):
        super().__init__()

        self.length = length
        self.width = width
        self.pos = vec(pos) - vec(0, self.width)

        self.surf = pygame.Surface((self.length, self.width))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(topleft=self.pos)


class End(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[float, float], size=40):
        super().__init__()

        self.size = size
        self.pos = vec(pos) - vec(0, self.size)

        self.surf = pygame.Surface((self.size, self.size))
        if DEBUG:
            self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect(topleft=self.pos)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.surf = pygame.image.load("enemy.png")
        self.surf = pygame.transform.smoothscale(self.surf, (50, 50))
        position = (position[0], position[1]-40)
        self.rect = self.surf.get_rect(center=position)
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        # TODO: add bullet image
        self.surf = pygame.image.load("bullet.png")
        self.surf = pygame.transform.smoothscale(self.surf, (50, 50))
        position = (position[0], position[1]-40)
        self.rect = self.surf.get_rect(center=position)