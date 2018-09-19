#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from __future__ import print_function, division

import math
import turtle

# Create square
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

# Create polyline
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# create polygon
def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)

# create arc
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

# create circle
def circle(t, r):
    arc(t, r, 360)


if __name__ == '__main__':
    bob = turtle.Turtle()

    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    circle(bob, radius)

    turtle.mainloop()