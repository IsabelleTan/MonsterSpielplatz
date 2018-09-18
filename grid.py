class Grid(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [
            ['.' for _ in range(self.height)]
            for _ in range(self.width)]

    def add_monster(self, monster):
        x, y = monster.get_location()
        self.grid[20 - y][x] = 'X'

    def __str__(self):
        return '\n'.join([''.join(['{}'.format(item) \
                                   for item in row]) \
                                   for row in self.grid])