import sys
import pygame
from pygame.constants import *

pygame.init()
vec = pygame.math.Vector2  # 2 dimensional

# change any of these
HEIGHT = 450
WIDTH = 800
ACCEL = 0.5  # movement acceleration
FRICTION = -0.12  # friction
FPS = 60

frames_per_second = pygame.time.Clock()

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")  # you can change this

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))  # rgb
        self.rect = self.surf.get_rect()

        self.pos = vec(10, 400)
        self.vel = vec(0, 0)
        self.accel = vec(0, 0)

    def move(self):
        self.accel = vec(0, 0.5)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.accel.x = -ACCEL
        if pressed_keys[K_RIGHT]:
            self.accel.x = ACCEL

        self.accel.x += self.vel.x * FRICTION
        self.vel += self.accel
        self.pos += self.vel + 0.5 * self.accel

        if self.pos.y > HEIGHT:
            self.pos.x = 0
            self.pos.y = HEIGHT - 10

        self.rect.midbottom = self.pos

    def jump(self):
        self.vel.y = -15

    def update(self):
        #                               sprite  sprites  delete
        hits = pygame.sprite.spritecollide(P1, platforms, False)
        if hits:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0


class Platform(pygame.sprite.Sprite):
    position = ()
    length = ()

    def __init__(self, position, length):
        super().__init__()

        self.position = position
        self.length = length
        
        self.surf = pygame.Surface((length, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=position)


PT1 = Platform((0, HEIGHT), 200)
P1 = Player()

pts = [
    Platform((400, HEIGHT), 200),
    Platform((800, HEIGHT-100), 200),
    Platform((350, HEIGHT), 200)
]

platforms = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

platforms.add(PT1)
for pt in pts:
    platforms.add(pt)
    all_sprites.add(pt)

all_sprites.add(PT1)
all_sprites.add(P1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:  # challenge: can you make the up arrow jump too?
                P1.jump()

    display_surface.fill((0, 0, 0))

    P1.move()
    P1.update()

    for entity in all_sprites:
        display_surface.blit(entity.surf, entity.rect)

    pygame.display.update()
    frames_per_second.tick(FPS)