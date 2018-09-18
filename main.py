import numpy as np

from monster import *

grid_w = 20
grid_h = 20

erdbeerli1 = Erdbeerli(0, 0, grid_w, grid_h)
pirati1 = Pirati(0, 0, grid_w, grid_h)
brummi1 = Brummi(0, 0, grid_w, grid_h)
fressi1 = Fressi(0, 0, grid_w, grid_h)
glubschi1 = Glubschi(0, 0, grid_w, grid_h)
keksi1 = Keksi(0, 0, grid_w, grid_h)


for _ in range(3):
    erdbeerli1.step()
    pirati1.step()
    brummi1.step()
    fressi1.step()
    glubschi1.step()
    keksi1.step()

print(erdbeerli1)
print(pirati1)
print(brummi1)
print(fressi1)
print(glubschi1)
print(keksi1)