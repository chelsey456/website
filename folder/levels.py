from pygame import Vector2 as vec

from consts import HEIGHT, WIDTH
from objects import End, Platform


class Level:
    def __init__(self, start_position, platforms: list[Platform], end: End):
        self.start_position = vec(start_position)
        self.platforms = platforms
        self.end = end

        self.sprites = platforms + [end]


level1 = Level(
    start_position=(15, HEIGHT - 30),
    platforms=[
        Platform((0, HEIGHT)),
        Platform((400, HEIGHT), 200),
        Platform((800, HEIGHT-100), 200),
        Platform((350, HEIGHT), 200)
    ],
    end=End((WIDTH // 2 + 10, HEIGHT - 90)),
)

level2 = Level(
    start_position=(15, 0),
    platforms=[
        Platform((0, HEIGHT)),
        Platform((WIDTH // 2 - 60, HEIGHT - 70), length=100),
        Platform((WIDTH - 300, HEIGHT - 100), length=100),
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
    end=End((800, HEIGHT - 100)),
)

level4 = Level(
    start_position=(15, HEIGHT - 30),
    platforms=[
        Platform((0, HEIGHT)),
        Platform((350, HEIGHT), 50),
    ],
    end=End((800, HEIGHT - 100)),
)

levels = [x for x in list(vars().values()) if isinstance(x, Level)]
