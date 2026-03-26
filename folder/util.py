import pygame
from pygame.font import Font
from pygame.surface import Surface
from pygame.math import Vector2 as vec

from consts import FONT, WIDTH, HEIGHT
from objects import End, Platform


def text(text: str, font: Font = FONT) -> Surface:
    """renders text to a surface with a black background and white text"""
    return font.render(
        text,
        True,
        (255, 255, 255),
        (0, 0, 0),
    )


def fmt_obj(obj) -> str:
    """formats the attributes of an object in a readable format"""
    if isinstance(obj, Platform):
        return f"l:{obj.length} w:{obj.width}"
    elif isinstance(obj, End):
        return f"s:{obj.size}"
    else:
        return "Unknown object!"


def transform(pos, cam):
    """turn world coordinates into screen coordinates"""
    cam = max(0, cam)
    if isinstance(pos, vec):
        return pos - vec(cam, 0)
    if isinstance(pos, pygame.Rect):
        return pos.topleft - vec(cam, 0)
    return pos - cam


def debug(
    display,
    player,
    all_sprites,
    level,
    show_grid_lines,
    show_entity_info,
    world_info: str | None = None,
    cam: float | None = None,
):
    """ "renders debug info to the screen"""

    scrolling = cam is not None

    if show_grid_lines:
        for x in range(0, WIDTH, 20):
            pygame.draw.line(display, (0, 120, 20), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, 20):
            pygame.draw.line(display, (0, 120, 20), (0, y), (WIDTH, y))

        for x in range(0, WIDTH, 60):
            pygame.draw.line(display, (0, 20, 170), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, 60):
            pygame.draw.line(display, (0, 20, 170), (0, y), (WIDTH, y))

    if world_info:
        display.blit(text(world_info), (WIDTH - text(world_info).get_width() - 10, 10))

    if scrolling:
        p_pos = text(f"pos: ({player.pos.x:.2f}, {player.pos.y:.2f}) scr({transform(player.pos.x, cam):.2f})")
    else:
        p_pos = text(f"pos: ({player.pos.x:.2f}, {player.pos.y:.2f})")
    display.blit(p_pos, (10, 10))

    p_vel = text(f"vel: ({player.vel.x:.2f}, {player.vel.y:.2f})")
    display.blit(p_vel, (10, 30))

    if scrolling:
        cam_text = text(f"cam: {cam:.2f}")
        display.blit(cam_text, (10, 50))

    collisions = pygame.sprite.spritecollide(player, level, False)  # type: ignore
    if collisions:
        if scrolling:
            collision_text = text(f"on: {', '.join([f'{c.pos} scr({transform(c.pos.x, cam):.2f}), {fmt_obj(c)}' for c in collisions])}")
        else:
            collision_text = text(f"on: {', '.join([f'{c.pos}, {fmt_obj(c)}' for c in collisions])}")
        display.blit(collision_text, (10, 70 if scrolling else 50))

    cursor_pos = vec(pygame.mouse.get_pos())
    if scrolling:
        cursor = text(f"{cursor_pos} scr({transform(cursor_pos.x, cam):.2f})")
    else:
        cursor = text(f"{cursor_pos}")
    display.blit(cursor, (cursor_pos.x + 1, cursor_pos.y - 15))

    for entity in all_sprites:
        if entity == player:
            continue

        if scrolling:
            info = text(f"> {entity.pos} scr({transform(entity.pos.x, cam):.2f}), {fmt_obj(entity)}")
        else:
            info = text(f"> {entity.pos}, {fmt_obj(entity)}")

        if show_entity_info:
            if scrolling:
                display.blit(info, transform(vec(entity.pos.x, entity.pos.y - 15), cam))
            else:
                display.blit(info, (entity.pos.x, entity.pos.y - 15))
        else:
            cursor = pygame.Rect((cursor_pos.x, cursor_pos.y - 10), (20, 20))

            if cursor.colliderect(entity.rect):
                display.blit(info, (cursor_pos.x + 1, cursor_pos.y - 15))
