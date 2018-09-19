class Grid(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [
            ['.' for _ in range(self.height)]
            for _ in range(self.width)]
        self.monsters = []

    def add_monster(self, monster):
        self.monsters.append(monster)

    def __str__(self):
        for monster in self.monsters:
            x, y = monster.get_location()
            self.grid[20 - y][x] = monster.__class__.__name__[0]
        return '\n'.join([' '.join(['{}'.format(item) \
                                   for item in row]) \
                                   for row in self.grid])