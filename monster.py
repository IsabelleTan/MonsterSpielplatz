import abc
from itertools import cycle


class Monster(object, metaclass=abc.ABCMeta):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid_w = 1
        self.grid_h = 1
        self.jump_size = 0
        self.jump_pattern = cycle(())
        self.letters = ''

    def step(self):
        step_x, step_y = (next(self.jump_pattern))
        self.x += step_x
        self.y += step_y

        self.x %= self.grid_w
        self.y %= self.grid_h

    def set_grid_size(self, grid_w, grid_h):
        self.grid_w = grid_w
        self.grid_h = grid_h

    def get_location(self):
        return self.x, self.y

    def jump(self):
        for _ in range(self.jump_size):
            self.step()

    def set_jump(self, jump):
        self.jump_size = len(jump)
        self.jump_pattern = cycle(jump)

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __str__(self):
        return "{} at ({}, {}) in Grid ({}, {})"\
                .format(__class__.__name__, self.x, self.y, self.grid_w, self.grid_h)


class Erdbeerli(Monster):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.set_jump(((-1, 1), (2, 2), (-2, 0)))


class Pirati(Monster):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.set_jump(((1, 1), (-1, 2), (-2, -2)))


class Brummi(Monster):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.set_jump(((4, 2), (4, 0), (1, 0)))


class Fressi(Monster):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.set_jump(((1, 1), (-4, 0), (-1, -1)))


class Glubschi(Monster):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.set_jump(((-1, 1), (-2, -1), (2, 0)))


class Keksi(Monster):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.set_jump(((0, -2), (2, 0), (0, -1)))
