import numpy as np

from monster import *

erdbeerli1 = Erdbeerli(0, 0, 20, 20)

print(erdbeerli1)
for _ in range(7):
    erdbeerli1.step()
    print(erdbeerli1)