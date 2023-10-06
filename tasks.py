import random
import math
import itertools

def generate_quadrilaterals(n, x, y):
    quadrilaterals = []
    while len(quadrilaterals) < n:
        
        random_x = random.uniform(0, x)
        random_y = random.uniform(0, y)

        diff_x = x / 10
        diff_y = y / 10

        x_low = random_x - diff_x

        if x_low < 0:
            x_low = 0
        x_top = random_x + diff_x
        if x_top > x:
            x_top = x
        
        y_low = random_y - diff_y
        if y_low < 0:
            y_low = 0

        y_top = random_y + diff_y
        if y_top > y:
            y_top = y
        q = [(random.uniform(x_low, x_top), random.uniform(y_low, y_top)) for _ in range(4)]
        if len(set(q)) != 4:
            continue
        for permutation in itertools.permutations(q):
            if is_convex_quadrilateral(permutation):
                q = permutation
                break
        if not check_angles(q):
            continue
        intersects = False
        for q1 in quadrilaterals:
            intersects = intersects_quadrilaterals(q, q1)
            if intersects == True:
                break
        if not intersects and is_convex_quadrilateral(q):
            quadrilaterals.append(q)

    return quadrilaterals
def intersect(line1_start, line1_end, line2_start, line2_end):
    """
    Перевірка перетину двох відрізків

    :param line1_start: початкова точка першого відрізка
    :param line1_end: кінцева точка першого відрізка
    :param line2_start: початкова точка другого відрізка
    :param line2_end: кінцева точка другого відрізка
    :return: True якщо відрізки перетинаються, False - у іншому випадку
    """

    # Знаходимо вектори для двох відрізків
    p = (line1_start[0], line1_start[1])
    r = (line1_end[0] - line1_start[0], line1_end[1] - line1_start[1])
    q = (line2_start[0], line2_start[1])
    s = (line2_end[0] - line2_start[0], line2_end[1] - line2_start[1])

    # Знаходимо знаменник t та u
    denominator = r[0] * s[1] - r[1] * s[0]
    if denominator == 0:
        return False

    t = ((q[0] - p[0]) * s[1] - (q[1] - p[1]) * s[0]) / denominator
    u = ((q[0] - p[0]) * r[1] - (q[1] - p[1]) * r[0]) / denominator

    # Перевіряємо, чи лежать точки перетину відрізків на відрізках
    if t >= 0 and t <= 1 and u >= 0 and u <= 1:
        return True

    return False

def intersects_quadrilaterals(q1, q2):
    lines1 = [
        (q1[0], q1[1]),
        (q1[1], q1[2]),
        (q1[2], q1[3]),
        (q1[3], q1[0])
    ]

    lines2 = [
        (q2[0], q2[1]),
        (q2[1], q2[2]),
        (q2[2], q2[3]),
        (q2[3], q2[0])
    ]

    for i in range(len(lines1)):
        for j in range(len(lines2)):
            if intersect(lines1[i][0], lines1[i][1], lines2[j][0], lines2[j][1]):
                return True

    return False
# def is_convex_quadrilateral(points):
#     n = len(points)
#     sign = None
#     for i in range(n):
#         x1, y1 = points[i]
#         x2, y2 = points[(i + 1) % n]
#         x3, y3 = points[(i + 2) % n]
#         # Векторні добутки
#         cross_product = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
#         # Перевірка на зміну знаків
#         if sign is None:
#             sign = cross_product > 0
#         elif sign != (cross_product > 0):
#             return False
#     return True
def is_convex_quadrilateral(vertices):
    # Перевірка наявності чотирьох вершин
    if len(vertices) != 4:
        return False
    
    # Перевірка, чи всі внутрішні кути менші за 180 градусів
    vectors = []
    for i in range(4):
        v1 = (vertices[i][0] - vertices[(i-1)%4][0], vertices[i][1] - vertices[(i-1)%4][1])
        v2 = (vertices[(i+1)%4][0] - vertices[i][0], vertices[(i+1)%4][1] - vertices[i][1])
        vectors.append(v1[0]*v2[1] - v1[1]*v2[0])
    
    if all(v > 0 for v in vectors) or all(v < 0 for v in vectors):
        return True
    else:
        return False

def check_angles(vertices):
    # перевірка чи кількість вершин дорівнює 4
    if len(vertices) != 4:
        return False
    
    # визначення кутів чотирикутника
    angles = []
    for i in range(4):
        p1 = vertices[i]
        p2 = vertices[(i+1)%4]
        p3 = vertices[(i+2)%4]
        
        v1 = (p1[0]-p2[0], p1[1]-p2[1])
        v2 = (p3[0]-p2[0], p3[1]-p2[1])
        
        dot_product = v1[0]*v2[0] + v1[1]*v2[1]
        magnitude_v1 = math.sqrt(v1[0]**2 + v1[1]**2)
        magnitude_v2 = math.sqrt(v2[0]**2 + v2[1]**2)
        
        angle = math.acos(dot_product / (magnitude_v1 * magnitude_v2))
        angles.append(angle)
    
    # перевірка кутів на меншість за 150 градусів
    for angle in angles:
        if angle > math.radians(150):
            return False
    
    return True