from collections import namedtuple
import numpy as np
from sklearn.cluster import SpectralClustering, DBSCAN
from sklearn.preprocessing import StandardScaler
import png

from monster import *

Color = namedtuple('Color', ['R', 'G', 'B'])

class MonsterRecognition(object):
    def __init__(self, filename):
        self.filename = filename
        self.monsters = []
        self.rgba_image = []
        self.rgb_image = []
        self.model = []
        self.number_to_monster = {
            1: Erdbeerli,
            2: Fressi,
            3: Brummi,
            4: Glubschi,
            5: Pirati,
            6: Keksi,
        }

    def train_monster_recognition_model(self):
        """Train the monster recognition clustering model."""
        standarized_data = self.prepare_image_data(
            './monsterspielplatz3_tiny.png')
        self.model = DBSCAN(eps=0.5, min_samples=5)\
            .fit(standarized_data)

        return self.model

    def find_monsters(self):
        standarized_data = self.prepare_image_data(self.filename)

        monsters = self.dbscan_predict(
            self.model,
            standarized_data)

        monsters = np.reshape(monsters, (21, 21))
        monsters = np.rot90(monsters)

        for y, row in enumerate(reversed(monsters)):
            for x, number in enumerate(row):
                if number > 0:
                    self.monsters.append(
                        self.number_to_monster[number](x, y))

        return self.monsters

    def prepare_image_data(self, filename):
        self.rgb_image = self.read_png(filename)
        unrolled_data = [color for row in self.rgb_image for color in row]

        return self.standarize_data(unrolled_data)

    def read_png(self, filename):
        png_data = png.Reader(filename=filename).read()
        self.rgba_image = np.vstack(png_data[2])
        self.rgb_image = self.convert_rgba_to_rgb()

        return self.rgb_image

    def convert_rgba_to_rgb(self):
        size = len(self.rgba_image)
        self.rgb_image = np.zeros((size, size), dtype=(int, 3))
        for y in reversed(range(size)):
            for x in range(size):
                self.rgb_image[x, y] = self.get_color(x, y)

        return self.rgb_image

    def get_color(self, x, y):
        """Return the color of the pixel at the x, y coordinates."""
        row = self.rgba_image[20 - y]
        color = Color(*row[x * 4: x * 4 + 3])

        return color

    def dbscan_predict(self, model, X):
        """
        Source: https://stackoverflow.com/a/51516334/6329629
        """
        nr_samples = X.shape[0]

        y_new = np.ones(shape=nr_samples, dtype=int) * -1

        for i in range(nr_samples):
            diff = model.components_ - X[i, :]  # NumPy broadcasting

            dist = np.linalg.norm(diff, axis=1)  # Euclidean distance

            shortest_dist_idx = np.argmin(dist)

            if dist[shortest_dist_idx] < model.eps:
                y_new[i] = model.labels_[
                    model.core_sample_indices_[shortest_dist_idx]]

        return y_new

    def standarize_data(self, data):
        return StandardScaler().fit_transform(data)

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



