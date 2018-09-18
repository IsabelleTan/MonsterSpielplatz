from monster import *
from grid import *

grid_w = 21
grid_h = 21

grid = Grid(grid_w, grid_h)

# All monster coordinates for Monsterspielplatz 1
erdbeerlis = [(5, 15), (7, 15), (14, 15),
              (20, 15), (8, 14), (19, 14),
              (7, 13), (8, 13), (15, 13),
              (17, 12), (4, 11), (17, 11),
              (2, 10), (20, 9), (1, 7),
              (7, 7), (14, 7), (4, 6),
              (8, 6), (17, 5), (6, 4),
              (15, 4), (13, 3), (13, 2),
              (17, 2), (15, 1), (16, 1)]
piratis = [(7, 0), (17, 1), (8, 2), (4, 3),
           (8, 3), (1, 6), (6, 6), (0, 13),
           (8, 15), (17, 15), (0, 16), (7, 16),
           (5, 19), (16, 19)]
brummis = [(9, 1), (0, 3), (10, 3), (12, 3),
           (4, 4), (8, 4), (1, 11), (9, 12), (12, 12),
           (1, 14), (13, 14), (14, 14), (16, 14), (20, 14),
           (4, 15), (7, 16), (3, 19), (6, 20), (12, 20)]
fressis = [(1, 1), (20, 2), (1, 4), (13, 4), (14, 4),
           (20, 4), (5, 7), (1, 8), (14, 10), (4, 17),
           (1, 19), (0, 20), (19, 20)]
glubschis = [(0, 7), (12, 8), (9, 10), (15, 10),
                 (11, 11), (1, 13), (2, 13), (17, 16),
                 (9, 17), (9, 19)]
keksis = [(5, 2), (6, 2), (19, 2), (7, 3),
          (4, 5), (12, 6), (18, 6), (5, 8),
          (0, 10), (18, 10), (7, 11), (12, 11),
          (4, 12), (19, 12), (3, 14), (13, 14),
          (15, 14), (15, 16)]

monsters = []

for erdbeerli in erdbeerlis:
    monsters.append(Erdbeerli(*erdbeerli, grid_w, grid_h))
for pirati in piratis:
    monsters.append(Pirati(*pirati, grid_w, grid_h))
for brummi in brummis:
    monsters.append(Brummi(*brummi, grid_w, grid_h))
for fressi in fressis:
    monsters.append(Fressi(*fressi, grid_w, grid_h))
for glubschi in glubschis:
    monsters.append(Glubschi(*glubschi, grid_w, grid_h))
for keksi in keksis:
    monsters.append(Keksi(*keksi, grid_w, grid_h))

for monster in monsters:
    for _ in range(10):
        monster.jump()
    grid.add_monster(monster)

print(grid)