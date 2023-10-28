def no_paths(L):
    return len(L)

def no_points(L):
    return sum([len(l) for l in L])

def width(L):
    w=0
    for i in range(no_paths(L)):
        width = max([l[0] for l in L[i]]) - min([l[0] for l in L[i]])
        if width > w:
            w = width
    return w

def height(L):
    h=0
    for i in range(no_paths(L)):
        height = max([l[1] for l in L[i]]) - min([l[1] for l in L[i]])
        if height > h:
            h = height
    return h