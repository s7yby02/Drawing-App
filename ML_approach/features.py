from scipy.spatial import ConvexHull
import numpy as np

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

def height(draw: list[list[int]])-> int:
    """
    It calculates the height of the shape
    """
    maxi, mini = 0, 0
    for i in range(no_paths(draw)):
        maxi = max(max([l[1] for l in draw[i]]), maxi)
        mini = min(max([l[1] for l in draw[i]]), mini)
    return maxi - mini

def elongation(draw):
    """
    It calculates the elongation of the shape.
    Elongation is a measure of how much a shape extends in one direction compared to its perpendicular direction.
    """
    w, h = width(draw), height(draw)
    return (1 + max(w,h))/(1 + min(w,h))

def get_hull_shape(shape):
    """
    It returns the smallest envellope of points that englobe the shape.
    """
    points = [ [point[0], 400-point[1]] for path in shape for point in path ]
    points = np.array(points)
    hull = ConvexHull(points)
    envelop_points = hull.points[hull.vertices]
    return envelop_points

def get_distance(A,B):
    """
    It calculates the distance between two point (euclidien distance).
    """
    from math import sqrt
    xa, ya = A
    xb, yb = B
    return sqrt((xb - xa)**2 + (yb - ya)**2)

def get_length(points):
    """
    It calculates the lenght(perimeter) of an array of points that forme a cycle (elmnt_1->elmnt_2->...->elmnt_n->elmnt_1).
    """
    length = 0
    for ip in range(len(points)):
        p0 = points[ip]
        p1 = points[(1+ip)%len(points)]
        length+= get_distance(p0, p1)
    return length

def get_length2(shape):
    """
    It calculates the lenght(perimeter) of the hull around the shape(the smallest envellope of points that englobe the shape).
    """
    hull_points = get_hull_shape(shape)
    length = get_length(hull_points)
    return length

def triangle_area(A,B,C):
    """
    It calculates the area of a triangle.
    """
    a = get_distance(A,B)
    b = get_distance(B,C)
    c = get_distance(C,A)
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**.5

def get_area(points):
    """
    It calculates the area of the points.
    """
    area = 0
    A = points[0]
    for ip in range(1,len(points)-1):
        B = points[ip]
        C = points[ip + 1]
        area += triangle_area(A, B, C)
    return area

def get_area2(shape):
    """
    It calculates the area of the shape.
    """
    hull_points = get_hull_shape(shape)
    area = get_area(hull_points)
    return area

def get_roundness(shape):
    """
    It calculates the roundness of the shape.
    Roundness is a measure of how closely the shape of an object approaches that of a mathematically perfect circle.
    """
    from math import pi
    hull_points = get_hull_shape(shape)
    length = get_length(hull_points)
    area = get_area(hull_points)
    R = length/(2*pi)
    circle_area = pi*R**2
    roundness = area/circle_area
    return roundness