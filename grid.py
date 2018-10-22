class Grid(object):
    def __init__(self, width, height, letter_grid):
        self.width = width
        self.height = height
        self.monsters = []
        self.letter_grid = letter_grid
        self.e_letters = ''
        self.n_letters = ''

    def add_monster(self, monster):
        monster.set_grid_size(self.width, self.height)
        self.monsters.append(monster)

    def do_step(self):
        for monster in self.monsters:
            monster.step()
            mon_x, mon_y = monster.get_location()
            letter = self.letter_grid.pop((mon_x, mon_y), '')
            if monster.__class__.__name__[0] in ['E', 'B', 'G']:
                self.n_letters += letter
            else:
                self.e_letters += letter

    def do_jump(self):
        for monster in self.monsters:
            monster.jump()

    def plot(self):
        return NotImplemented


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
