import math


def is_convex_quadrilateral(points):

    if len(set(points)) != 4:
        return 0

    center_x = sum(x for x, y in points) / 4
    center_y = sum(y for x, y in points) / 4
    points.sort(key=lambda p: (math.atan2(p[1] - center_y, p[0] - center_x)))

    def cross_product_sign(o, a, b):

        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    signs = []
    for i in range(4):
        o = points[i]
        a = points[(i + 1) % 4]
        b = points[(i + 2) % 4]
        signs.append(cross_product_sign(o, a, b))

    return 1 if all(s > 0 for s in signs) or all(s < 0 for s in signs) else 0


with open("input.txt", "r") as f:
    points = [tuple(map(int, line.split())) for line in f]

print(is_convex_quadrilateral(points))
