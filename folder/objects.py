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
    def __init__(self, pos):
        super().__init__()

        self.surf = pygame.image.load("enemy.png")
        self.surf = pygame.transform.smoothscale(self.surf, (50, 50))
        pos = (pos[0], pos[1]-40)
        self.pos = vec(pos)
        self.rect = self.surf.get_rect(center=pos)
        
class Coin(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[float, float]):
        super().__init__()

        self.pos = vec(pos)

        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255, 255, 0))
        self.rect = self.surf.get_rect(topleft=self.pos)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, vel):
        super().__init__()

        self.vel = vec(vel)

        # TODO: add bullet image
        self.surf = pygame.image.load("bullet.png")
        self.surf = pygame.transform.smoothscale(self.surf, (50, 15))
        self.pos = vec(pos)
        self.rect = self.surf.get_rect(center=pos)

    def update(self):
        self.pos += self.vel
        self.rect.topleft = self.pos

        
# class Enemy(pygame.sprite.Sprite):
#     def __init__(self, pos: tuple[float, float], size=30):
#         super().__init__()
#         self.size = size
#         self.pos = vec(pos) - vec(0, self.size)

#         self.surf = pygame.Surface((self.size, self.size))
#         self.surf.fill((255, 0, 200))
#         self.rect = self.surf.get_rect(topleft=self.pos)
        
# class Bullet(pygame.sprite.Sprite):
#     def __init__(self, pos: tuple[float, float], vel: vec):
#         super().__init__()
#         self.vel = vel
#         self.pos = vec(pos)

#         self.surf = pygame.Surface((10, 10))
#         self.surf.fill((255, 255, 0))
#         self.rect = self.surf.get_rect(topleft=self.pos)
    
    