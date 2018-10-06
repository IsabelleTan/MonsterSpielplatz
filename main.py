from monster import *
from grid import *

grid_w = 21
grid_h = 21

grid = Grid(grid_w, grid_h)

# All monster coordinates for Monsterspielplatz 1
brummis = [
    (6, 0), (0, 1), (20, 2), (14, 9), (17, 9), (19, 10), (15, 10), (5, 12),
    (11, 15), (17, 17), (20, 17), (6, 20),
]
erdbeerlis = [
    (15, 4), (9, 5), (17, 5), (18, 6), (7, 7), (8, 7), (0, 8), (8, 10),
    (6, 17), (13, 10), (9, 18), (19, 19), (5, 19),
    ]
fressis = [
    (1, 3), (4, 4), (2, 5), (8, 5), (20, 6), (12, 7), (20, 7), (11, 8), (2, 9),
    (7, 9), (6, 11), (2, 13), (6, 13), (19, 14), (10, 16), (11, 17),
    ]
glubschis = [
    (1, 4), (17, 4), (11, 9), (17, 10), (16, 10), (2, 10), (2, 12), (9, 13),
    (17, 15), (3, 15), (13, 18)
 ]
keksis = [
    (5, 1), (9, 1), (18, 1), (19, 1), (1, 2), (2, 2), (4, 2), (9, 3), (19, 4),
    (2, 6), (4, 6), (8, 6), (17, 6), (19, 6), (3, 7), (9, 9), (3, 10), (2, 11),
    (18, 11), (9, 12), (2, 19), (9, 19), (18, 19), (16, 20),
    ]
piratis = [
    (10, 5), (11, 5), (3, 9), (1, 10), (5, 11), (1, 13), (18, 13), (11, 13),
    (16, 15), (3, 18)
]

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
    grid.add_monster(monster)

for _ in range(7):
    grid.do_step()

print(grid)
