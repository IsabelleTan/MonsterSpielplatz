import numpy as np
import png

from collections import namedtuple

Color = namedtuple('Color', ['R', 'G', 'B'])

class MonsterRecognition(object):
    def __init__(self, filename):
        self.filename = filename
        self.monsters = []
        self.image_2d = []

    def read_png(self):
        pngdata = png.Reader(filename=self.filename).read()
        self.image_2d = np.vstack(pngdata[2])

        return self.image_2d

    def get_id(self, color):
        """Return a number which can be used to map pixel to a monster."""
        id = (color.R.astype(np.int32)
            * color.G.astype(np.int32)
            * color.B.astype(np.int32))
        return id

    def get_color(self, x, y):
        """Return the color of the pixel at the x, y coordinates."""
        row = self.image_2d[20 - y]
        color = Color(*row[x * 4 : x * 4 + 3])

        return color

    def get_monsters(self):
        """Return a list with Monster objects which represent all found
        monsters in the image.
        """
        self.read_png()

        return NotImplemented


# def test_get_color():
#     m = MonsterRecognition('./monsterspielplatz3_tiny.png')
#     img = m.read_png()
#
#     actuals = [
#         tuple(m.get_color(4, 1)),
#         tuple(m.get_color(14, 2)),]
#     expecteds = [
#         (174, 193, 214),
#         (225, 210, 177),]
#     for act, exp in zip(actuals, expecteds):
#         assert act == exp, "{} not equal to {}".format(act, exp)



