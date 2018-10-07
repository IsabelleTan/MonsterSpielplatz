import abc
from itertools import cycle


class Monster(object, metaclass=abc.ABCMeta):
    def __init__(self, x, y, grid_w, grid_h):
        self.x = x
        self.y = y
        self.grid_w = grid_w
        self.grid_h = grid_h
        self.jump_size = 0
        self.jump_pattern = cycle(())

    def step(self):
        step_x, step_y = (next(self.jump_pattern))
        self.x += step_x
        self.y += step_y

        self.x %= self.grid_w
        self.y %= self.grid_h

    def get_location(self):
        return self.x, self.y

    def jump(self):
        for _ in range(self.jump_size):
            self.step()

    def set_jump(self, jump):
        self.jump_size = len(jump)
        self.jump_pattern = cycle(jump)

    def __str__(self):
        return "x: {}, y: {}. Grid width: {}, grid height: {}"\
                .format(self.x, self.y, self.grid_w, self.grid_h)


class Erdbeerli(Monster):
    def __init__(self, x, y, grid_w, grid_h):
        super().__init__(x, y, grid_w, grid_h)
        self.set_jump(((-1, 1), (2, 2), (-2, 0)))


class Pirati(Monster):
    def __init__(self, x, y, grid_w, grid_h):
        super().__init__(x, y, grid_w, grid_h)
        self.set_jump(((1, 1), (-1, 2), (-2, -2)))


class Brummi(Monster):
    def __init__(self, x, y, grid_w, grid_h):
        super().__init__(x, y, grid_w, grid_h)
        self.set_jump(((4, 2), (4, 0), (1, 0)))


class Fressi(Monster):
    def __init__(self, x, y, grid_w, grid_h):
        super().__init__(x, y, grid_w, grid_h)
        self.set_jump(((1, 1), (-4, 0), (-1, -1)))


class Glubschi(Monster):
    def __init__(self, x, y, grid_w, grid_h):
        super().__init__(x, y, grid_w, grid_h)
        self.set_jump(((-1, 1), (-2, -1), (2, 0)))


class Keksi(Monster):
    def __init__(self, x, y, grid_w, grid_h):
        super().__init__(x, y, grid_w, grid_h)
        self.set_jump(((0, -2), (2, 0), (0, -1)))
