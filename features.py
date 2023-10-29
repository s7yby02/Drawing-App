def no_paths(draw):
    return len(draw)

def no_points(draw):
    return sum([len(l) for l in draw])

def width(draw):
    w=0
    for i in range(no_paths(draw)):
        width = max([l[0] for l in draw[i]]) - min([l[0] for l in draw[i]])
        if width > w:
            w = width
    return w

def height(draw):
    h=0
    for i in range(no_paths(draw)):
        height = max([l[1] for l in draw[i]]) - min([l[1] for l in draw[i]])
        if height > h:
            h = height
    return h

def lenght(draw):
    l=0
    for i in range(no_paths(draw)):
        ...

def distance(A,B):
    from math import sqrt
    xa,ya = A
    xb,yb = B
    return sqrt((xb - xa)**2 + (yb - ya)**2)