def is_convex(points):
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    n = len(points)
    if n != 4:
        return 0

    if len(set(points)) != 4:
        return 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if orientation(points[i], points[j], points[k]) == 0:
                    return 0

    prev = orientation(points[0], points[1], points[2])
    for i in range(1, n):
        curr = orientation(points[i], points[(i + 1) % n], points[(i + 2) % n])
        if curr != prev:
            return 0
        prev = curr

    return 1

points = []
for _ in range(4):
    x, y = map(int, input().split())
    points.append((x, y))

result = is_convex(points)
print(result)
