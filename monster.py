import abc
import numpy as np
from itertools import cycle


class Monster(object, metaclass=abc.ABCMeta):
    def __init__(self, x, y, grid_w, grid_h):
        self.x = x
        self.y = y
        self.grid_w = grid_w
        self.grid_h = grid_h
        self.jump_pattern = cycle(())

    def step(self):
        step_x, step_y = (next(self.jump_pattern))
        self.x += step_x
        self.y += step_y

    def __str__(self):
        return "x: {}, y: {}. Grid width: {}, grid height: {}".format(self.x, self.y, self.grid_w, self.grid_h)


class Erdbeerli(Monster):
    def __init__(self, x, y, grid_w, grid_h):
        super().__init__(x, y, grid_w, grid_h)
        self.jump_pattern = cycle(((1, 2), (1, -2), (1, 0)))


class Pirati(Monster):
    def __init__(self, x, y, grid_w, grid_h):
        super().__init__(x, y, grid_w, grid_h)
        self.jump_pattern = cycle(((1, 2), (1, -1), (1, 2)))


class Brummi(Monster):
    def __init__(self, x, y, grid_w, grid_h):
        super().__init__(x, y, grid_w, grid_h)
        self.jump_pattern = cycle(((-1, -2), (3, 1), (-1, -1)))


class Fressi(Monster):
    def __init__(self, x, y, grid_w, grid_h):
        super().__init__(x, y, grid_w, grid_h)
        self.jump_pattern = cycle(((-1, 1), (-1, -2), (-1, 3)))


class Glubschi(Monster):
    def __init__(self, x, y, grid_w, grid_h):
        super().__init__(x, y, grid_w, grid_h)
        self.jump_pattern = cycle(((-1, 1), (0, -3), (-1, 1)))

class Keksi(Monster):
    def __init__(self, x, y, grid_w, grid_h):
        super().__init__(x, y, grid_w, grid_h)
        self.jump_pattern = cycle(((-1, 1), (-1, -2), (-1, 1)))
