"""
Animation of exp(j+2*pi*n*k/N) where N=8, k=0,1,2,3
"""

import math
import rendering

ScrW, ScrH = 600, 200

class Clock:
    def __init__(self, cx, cy, col=(0,1,0), rad=10):
        self.start = (cx, cy)
        self.end = (cx + rad, cy)
        self.rad = rad
        self.shape = rendering.make_circle(cx, cy, radius=rad)
        self.shape.set_color(*col)

class Shaft:
    def __init__(self, start, end):
        viewer.add_geom(rendering.Line(start, end))

    def update(self, i):
        x, y = self.start
        self.end = (x + r * math.cos(math.pi * i / 8 * 0), y + r * math.sin(math.pi * i / 8 * 0))


viewer = rendering.Viewer(ScrW, ScrH)
viewer.set_bgcolor(0,.5,.9)

ck1 = Clock(60,100,rad=60)
ck2 = Clock(180,100,rad=60)
ck3 = Clock(300,100,rad=60)
ck4 = Clock(420,100,rad=60)
ck5 = Clock(540,100,rad=60)
viewer.add_geom(ck1.shape)
viewer.add_geom(ck2.shape)
viewer.add_geom(ck3.shape)
viewer.add_geom(ck4.shape)
viewer.add_geom(ck5.shape)

l1 = rendering.Line(ck1.start,ck1.end)
l2 = rendering.Line(ck2.start,ck2.end)
l3 = rendering.Line(ck3.start,ck3.end)
l4 = rendering.Line(ck4.start,ck4.end)
l5 = rendering.Line(ck5.start,ck5.end)
viewer.add_geom(l1)
viewer.add_geom(l2)
viewer.add_geom(l3)
viewer.add_geom(l4)
viewer.add_geom(l5)



for i in range(10000):
    i = int(i/10)
    r = 60
    x, y = l1.start
    l1.end = (x + r*math.cos(math.pi * 2*i/8 * 0), y + r*math.sin(math.pi * 2*i/8 * 0))
    x, y = l2.start
    l2.end = (x + r*math.cos(math.pi * 2*i/8 * 1), y + r*math.sin(math.pi * 2*i/8 * 1))
    x, y = l3.start
    l3.end = (x + r*math.cos(math.pi * 2*i/8 * 2), y + r*math.sin(math.pi * 2*i/8 * 2))
    x, y = l4.start
    l4.end = (x + r*math.cos(math.pi * 2*i/8 * 3), y + r*math.sin(math.pi * 2*i/8 * 3))
    x, y = l5.start
    l5.end = (x + r*math.cos(math.pi * 2*i/8 * 4), y + r*math.sin(math.pi * 2*i/8 * 4))
    viewer.render()
