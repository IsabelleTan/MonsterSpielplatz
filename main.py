from grid import *
from monster import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import object_recognition
import importlib
importlib.reload(object_recognition)
from object_recognition import MonsterRecognition


# grid_w = 21
# grid_h = 21
#
# letter_grid = {(0, 0): 'H', (7, 0): 'A', (16, 0): 'U', (19, 0): 'W', (2, 1): 'L',
#                (5, 1): 'S', (17, 1): 'H', (20, 1): 'E', (3, 2): 'S',
#                (7, 2): 'D',
#                (19, 2): 'V',
#                (2, 3): 'B',
#                (6, 3): 'E',
#                (18, 3): 'N',
#                (12, 4): 'F',
#                (14, 4): 'I',
#                (19, 4): 'F',
#                (9, 5): 'S',
#                (4, 6): 'E',
#                (11, 6): 'E',
#                (2, 7): 'F',
#                (12, 7): 'L',
#                (17, 7): 'E',
#                (20, 7): 'N',
#                (0, 8): 'U',
#                (6, 8): 'N',
#                (16, 8): 'I',
#                (2, 9): 'C',
#                (5, 9): 'R',
#                (13, 9): 'E',
#                (18, 9): 'L',
#                (4, 10): 'I',
#                (7, 10): 'Z',
#                (12, 10): 'U',
#                (15, 10): 'V',
#                (20, 10): 'H',
#                (2, 11): 'F',
#                (6, 11): 'U',
#                (8, 11): 'B',
#                (16, 11): 'S',
#                (3, 12): 'N',
#                (9, 12): 'E',
#                (11, 12): 'C',
#                (6, 13): 'N',
#                (14, 13): 'F',
#                (17, 13): 'U',
#                (20, 13): 'W',
#                (1, 14): 'F',
#                (5, 14): 'A',
#                (9, 14): 'S',
#                (16, 14): 'E',
#                (3, 15): 'D',
#                (14, 15): 'I',
#                (20, 15): 'U',
#                (1, 16): 'E',
#                (6, 16): 'I',
#                (13, 16): 'E',
#                (16, 16): 'V',
#                (19, 16): 'E',
#                (3, 17): 'N',
#                (11, 17): 'U',
#                (15, 17): 'N',
#                (18, 17): 'R',
#                (2, 18): 'E',
#                (13, 18): 'F',
#                (19, 18): 'N',
#                (3, 19): 'C',
#                (5, 19): 'N',
#                (17, 19): 'S',
#                (20, 19): 'L',
#                (1, 20): 'E',
#                (7, 20): 'N',
#                (11, 20): 'R',
#                (14, 20): 'L',
#                (19, 20): 'T'
#                }
#
#
# grid = Grid(grid_w, grid_h, letter_grid)
#
#
# n_iterations = 0
# while len(grid.letter_grid)>0 and n_iterations < 50:
#     grid.do_step()
#     n_iterations+=1

# print('N:', grid.n_letters)
# print('E:', grid.e_letters)

def test_monsterspielplatz4(monsters4):
    assert monsters4[0].__class__.__name__ == 'Keksi', \
        'First monster should be a Keksi, but is a {}'\
            .format(monsters4[i].__class__.__name__)
    assert len(monsters4) == 90, 'Found {} monsters, should be {}'\
        .format(len(monsters4), 90)

    print('All tests passed!')

m = object_recognition.MonsterRecognition('./monsterspielplatz4_tiny.png')
m.train_monster_recognition_model()

monsters = m.find_monsters()

test_monsterspielplatz4(monsters)

grid = Grid(21, 21, {})
for monster in monsters:
    grid.add_monster(monster)

grid.do_jump()
print(len(grid.monsters))

