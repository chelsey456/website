from pygame import Vector2 as vec

from consts import HEIGHT, WIDTH
from objects import End, Enemy, Platform


class Level:
    def __init__(self, start_position, platforms: list[Platform], end: End, enemies: list[Enemy] = []):
        self.start_position = vec(start_position)
        self.platforms = platforms
        self.end = end
        self.enemies = enemies

        self.sprites = platforms + [end] + enemies

level1 = Level(
    start_position=(15, HEIGHT - 30),
    platforms=[
        Platform((0, HEIGHT)),
        Platform((400, HEIGHT), 200),
        Platform((800, HEIGHT-100), 200),
        Platform((350, HEIGHT), 200)
    ],
    enemies=[
        Enemy((400, HEIGHT-100))
    ],
    end=End((1200, HEIGHT - 100)),
)

level2 = Level(
    start_position=(15, 0),
    platforms=[
        Platform((0, HEIGHT)),
        Platform((WIDTH // 2 - 60, HEIGHT - 70), length=100),
        Platform((WIDTH - 300, HEIGHT - 100), length=100),
    ],
    enemies=[
        Enemy((200, HEIGHT-100))
    ],
    end=End((WIDTH // 2 + 300, HEIGHT - 90)),
)

level3 = Level(
    start_position=(15, HEIGHT - 30),
    platforms=[
        Platform((0, HEIGHT)),
        Platform((350, HEIGHT), 50),
        Platform((500, HEIGHT), 50),
    ],
       enemies=[
        Enemy((350, HEIGHT-100)),
        Enemy((500, HEIGHT-100)),
    ],
    end=End((800, HEIGHT - 100)),
)

level4 = Level(
    start_position=(15, HEIGHT - 30),
    platforms=[
        Platform((0, HEIGHT)),
        Platform((350, HEIGHT), 50),
    ],
       enemies=[
        Enemy((710, HEIGHT-100))
    ],
    end=End((800, HEIGHT - 100)),
)

level5 = Level(
    start_position=(15, HEIGHT - 30),
    platforms=[
        Platform((0, HEIGHT)),
    ],
    enemies=[
        Enemy((359, HEIGHT-100))
    ],
    end=End((600, HEIGHT - 100)),
)

levels = [x for x in list(vars().values()) if isinstance(x, Level)]

