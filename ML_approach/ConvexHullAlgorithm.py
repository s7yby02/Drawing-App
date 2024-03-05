#ConvexHull using "Jarvin March algorithm" (Gift-wrapping)
def orientation(A,B,C):
    xa, ya, xb, yb, xc, yc = *A, *B, *C
    return (yb - ya)*(xc - xa) - (yc - yb)*(xb - xa)

#if orientation(A,B,C) <0 : conterclockwise
#if orientation(A,B,C) >0 : clockwise
#if orientation(A,B,C) =0 : collinear

from features import distance
def convexhull(points):
    on_hull = min(points,key = lambda p : p[0])
    hull = []
    while 1 :
        hull.append(on_hull)
        next_point = points[0]
        for point in points:
            #print(point)
            o = orientation(on_hull,next_point,point)
            if o < 0 or next_point == on_hull or (
                o == 0 and distance(on_hull,point) > distance(on_hull,next_point)):
                
                next_point = point
        on_hull = next_point

        if on_hull == hull[0]:
            break
    return hull