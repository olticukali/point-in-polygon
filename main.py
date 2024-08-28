def is_point_in_polygon(point, vertices):
    x, y = point
    n = len(vertices)
    inside = False

    p1x, p1y = vertices[0]
    for i in range(n + 1):
        p2x, p2y = vertices[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside

point1 = (2, 5)
vertices = [(1, 2), (4, 8), (8, 6), (7, 1)]
print(f"Point {point1} is inside the polygon: {is_point_in_polygon(point1, vertices)}")

point2 = (6, 5)
print(f"Point {point2} is inside the polygon: {is_point_in_polygon(point2, vertices)}")
