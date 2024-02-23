def no_paths(draw: list[list[int]])-> int:
    """
    It calculates the number of lines to draw the shape
    """
    return len(draw)

def no_points(draw: list[list[int]])-> int:
    """
    It calculates the number of points to draw the shape
    """
    return sum([len(l) for l in draw])

def width(draw: list[list[int]])-> int:
    """
    It calculates the width of the shape
    """
    maxi, mini = 0, 0
    for i in range(no_paths(draw)):
        maxi = max(max([l[0] for l in draw[i]]), maxi)
        mini = min(max([l[0] for l in draw[i]]), mini)
    return maxi - mini

def height(draw)-> int:
    """
    It calculates the height of the shape
    """
    for i in range(no_paths(draw)):
        maxi = max(max([l[1] for l in draw[i]]), maxi)
        mini = min(max([l[1] for l in draw[i]]), mini)
    return maxi - mini

def elongation(draw):
    w, h = width(draw), height(draw)
    return (1 + max(w,h))/(1 + min(w,h))

def lenght(draw):
    l=0
    for i in range(no_paths(draw)):
        ...

def distance(A,B):
    from math import sqrt
    xa,ya = A
    xb,yb = B
    return sqrt((xb - xa)**2 + (yb - ya)**2)

def triangle_area(A,B,C):
    a = distance(A,B)
    b = distance(B,C)
    c = distance(C,A)
    p = (a+b+c)/2
    return (p*(p-a)(p-b)(p-c))**.5