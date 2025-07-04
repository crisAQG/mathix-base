from mathix import *


def distance(p1, p2):
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def manhattan_distance(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

def angle_between(v1, v2):
    dot = v1[0] * v2[0] + v1[1] * v2[1]
    mag1 = sqrt(v1[0] ** 2 + v1[1] ** 2)
    mag2 = sqrt(v2[0] ** 2 + v2[1] ** 2)
    return arccos(dot / (mag1 * mag2)) if mag1 and mag2 else 0

def rotate_point(px, py, cx, cy, angle_rad):
    s, c = sin(angle_rad), cos(angle_rad)
    px -= cx
    py -= cy
    xnew = px * c - py * s
    ynew = px * s + py * c
    return xnew + cx, ynew + cy

def line_intersects(p1, p2, q1, q2):


    def ccw(a, b, c):
        return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])

    return ccw(p1, q1, q2) != ccw(p2, q1, q2) and ccw(p1, p2, q1) != ccw(p1, p2, q2)

def point_in_polygon(point, polygon):
    global xints
    x, y = point
    inside = False
    n = len(polygon)
    px1, py1 = polygon[0]
    for i in range(n + 1):
        px2, py2 = polygon[i % n]
        if y > min(py1, py2):
            if y <= max(py1, py2):
                if x <= max(px1, px2):
                    if py1 != py2:
                        xints = (y - py1) * (px2 - px1) / (py2 - py1) + px1
                    if px1 == px2 or x <= xints:
                        inside = not inside
        px1, py1 = px2, py2
    return inside
