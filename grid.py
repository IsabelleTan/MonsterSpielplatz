import matplotlib.pyplot as plt

class Grid(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.monsters = []

    def add_monster(self, monster):
        self.monsters.append(monster)

    def do_step(self):
        for monster in self.monsters:
            monster.step()

    def do_jump(self):
        for monster in self.monsters:
            monster.jump()

    def plot(self):
        return None

    def __str__(self):
        grid = [
            ['.' for _ in range(self.height)]
            for _ in range(self.width)]
        for monster in self.monsters:
            x, y = monster.get_location()
            grid[self.height - 1 - y][x] = monster.__class__.__name__[0]
        return '\n'.join([' '.join(['{}'.format(item) \
                                   for item in row]) \
                                   for row in grid])
