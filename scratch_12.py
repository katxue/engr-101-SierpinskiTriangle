import numpy as np
import math
from math import cos, sin, pi
import random
import matplotlib.pyplot as plt

winx = 1000
winy = 1000
N = 8

mid = [winx / 2, winy / 2]

def calc_constant(N):
    times = N // 4
    bottom = 0
    if times > 0:
        for i in range(1, times+1):
            bottom = bottom + cos(2*pi*i/N)
    bottom = (bottom + 1) * 2
    constant = 1 / bottom
    return constant


def calc_vertices(winx, winy, N):
    mid = (winx/2, winy/2)
    radius = winy / 2
    angle = 2 * pi / N
    angles = [(angle * n) + (pi/2) for n in range(N)]
    vertices = [[radius * cos(a), radius * sin(a)] for a in angles]
    vertices = [(v[0] + mid[0], v[1] + mid[1]) for v in vertices]
    return vertices


def midpoint(p, q):
    return c * (p[0] + q[0]), c * (p[1] + q[1])


vertices = calc_vertices(winx, winy, N)
c = calc_constant(N)
radius = winy / 2

xp = random.randint(0, winx)
yp = random.randint(0, winy)
x = [xp]
y = [yp]
for i in range(100000):
   vert = np.random.randint(0, N)
   p = midpoint([xp, yp], vertices[vert])
   xp = p[0]
   yp = p[1]
   x.append(xp)
   y.append(yp)

plt.scatter(x, y, s=1, c='black')
plt.show()