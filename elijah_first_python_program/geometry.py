# This program contains functions that evaluate formulas used in geometry.
#
# Your Name
# August 22, 2014

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))

def parallelogram_area(b, h):
    a = b * h
    return a

def trapezoid_area ( a, b, h):
    a = a + b / 2 * h
    return a

def rectangular_prism_volume ( w, h, l):
    v = w*h*l
    return v

def cone_volume ( r, h):
    v = math.pi * r**2 * (h/3)
    return v


def sphere_volume ( r ):
    v = 4/3 * math.pi * r**3
    return v

def rectangular_prism_surface_area ( l, w, h):
    a = 2 * (w * l + h * l + h * w)
    return a

def sphere_suface_area ( r):
    a = 4 * math.pi * r**2
    return a

def pythagorean_theorem (a, b,):
    c = math.sqrt(a**2 + b**2)
    return c



