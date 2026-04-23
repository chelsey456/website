import sys
import pygame
from pygame.constants import (
    K_a,
    K_c,
    K_x,
    K_z,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    KMOD_CTRL,
    QUIT,
    KEYDOWN,
)
from pygame.math import Vector2 as vec

from levels import levels
from objects import Platform
from objects import Bullet, End, Enemy
from consts import DEBUG, WIDTH, HEIGHT, ACCEL, FRICTION, FPS
from util import debug, transform

pygame.init()

frames_per_second = pygame.time.Clock()

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")  # you can change this

level_num = 0
LEVEL = pygame.sprite.Group(levels[level_num].sprites)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))  # rgb
        self.rect = self.surf.get_rect()

        self.pos = vec(15, HEIGHT - 50)
        self.vel = vec(0, 0)
        self.accel = vec(0, 0)

        self.score = 0

    def move(self):
        self.accel = vec(0, 0.5)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.accel.x = -ACCEL
        if pressed_keys[K_RIGHT]:
            self.accel.x = ACCEL

        self.accel.x += self.vel.x * -FRICTION
        self.vel += self.accel
        self.pos += self.vel + 0.5 * self.accel

        self.rect.midbottom = self.pos  # type: ignore

    jumps = 0
    def jump(self):
        if self.jumps <= 1:
            self.jumps += 1
            self.vel.y = -15

    def update(self):
        #                                sprite  sprites  delete?
        hits = pygame.sprite.spritecollide(PLAYER, LEVEL, False)  # type: ignore
        for hit in hits:
            if isinstance(hit, Platform):
                self.jumps = 0
                if self.pos.x < hit.rect.left:
                    self.pos.x = hit.rect.left - self.surf.get_width() / 2
                    self.vel.x = 0
                elif self.pos.x > hit.rect.right:
                    self.pos.x = hit.rect.right + self.surf.get_width() / 2
                    self.vel.x = 0
                elif self.pos.y > hits[0].rect.bottom:
                    self.pos.y = (
                        hits[0].rect.bottom
                        + hits[0].surf.get_height()
                        + self.surf.get_height() / 2
                        + 1
                    )  # fmt: skip
                    self.vel.y = 0
                else:
                    self.pos.y = hits[0].rect.top + 1
                    self.vel.y = 0
            elif isinstance(hit, End):
                global level_num
                level_num += 1
                if level_num >= len(levels):
                    print("you win!")
                    pygame.quit()
                    sys.exit()
                setup_level()

        if self.pos.y > HEIGHT:
            self.pos = vec(15, HEIGHT - 50)

        # top left align
        if self.pos.x < self.surf.get_width() / 2:
            self.pos.x = self.surf.get_width() / 2
            self.vel.x = 0
        if self.pos.y < self.surf.get_height():
            self.pos.y = self.surf.get_height()
            self.vel.y = 0


PLAYER = Player()

BULLETS = []

ALL_SPRITES = pygame.sprite.Group()
ALL_SPRITES.add(PLAYER)
ALL_SPRITES.add(LEVEL)


def setup_level():
    global LEVEL

    print(f"loading level {level_num + 1}")

    LEVEL = pygame.sprite.Group(levels[level_num].sprites)

    ALL_SPRITES.empty()
    ALL_SPRITES.add(PLAYER)
    ALL_SPRITES.add(LEVEL)

    PLAYER.pos = levels[level_num].start_position
    PLAYER.vel = vec(0, 0)


setup_level()

# only horizontal
CAMERA = PLAYER.pos.x - WIDTH // 2

show_entity_info = False
show_grid_lines = True


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                PLAYER.jump()
            elif event.mod & KMOD_CTRL and event.key == K_c:
                pygame.quit()
                sys.exit()
            elif event.key == K_a:
                bullet = Bullet((PLAYER.pos.x + PLAYER.surf.get_width() / 2, PLAYER.pos.y - PLAYER.surf.get_height()), vec(5, 0))
                BULLETS.append(bullet)
                ALL_SPRITES.add(bullet)
            elif DEBUG:
                if event.key == K_z:
                    show_entity_info = not show_entity_info
                elif event.key == K_x:
                    show_grid_lines = not show_grid_lines

    display.fill((0, 0, 0))

    PLAYER.move()
    PLAYER.update()

    CAMERA += (PLAYER.pos.x - CAMERA - WIDTH // 2) * 0.05

    for bullet in BULLETS:
        bullet.update()
        collided = pygame.sprite.spritecollideany(bullet, LEVEL)
        if collided or bullet.pos.x - abs(CAMERA) > WIDTH or bullet.pos.x - CAMERA < 0:
            if isinstance(collided, End):
                continue
            if isinstance(collided, Enemy):
                PLAYER.score += 1
                collided.kill()
            bullet.kill()
            BULLETS.remove(bullet)

    for entity in ALL_SPRITES:
        display.blit(entity.surf, transform(entity.rect, CAMERA))

    if DEBUG:
        debug(display, PLAYER, ALL_SPRITES, LEVEL, show_grid_lines, show_entity_info, cam=CAMERA, world_info=f"Level {level_num + 1}")

    pygame.display.update()
    frames_per_second.tick(FPS)