import math

def count_intersections(line, objects):
    count = 0
    for obj in objects:
        x1, y1 = obj[0]
        x2, y2 = obj[1]
        x3, y3 = obj[2]
        x4, y4 = obj[3]

        if line_intersection(line, [(x1,y1),(x2,y2)]) or \
           line_intersection(line, [(x2,y2),(x3,y3)]) or \
           line_intersection(line, [(x3,y3),(x4,y4)]) or \
           line_intersection(line, [(x4,y4),(x1,y1)]):
            count += 1
    return count

def line_intersection(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    denominator = (y4 - y3)*(x2 - x1) - (x4 - x3)*(y2 - y1)
    numerator1 = (x4 - x3)*(y1 - y3) - (y4 - y3)*(x1 - x3)
    numerator2 = (x2 - x1)*(y1 - y3) - (y2 - y1)*(x1 - x3)

    if denominator == 0:
        return False
    else:
        u1 = numerator1 / denominator
        u2 = numerator2 / denominator
        if u1 >= 0 and u1 <= 1 and u2 >= 0 and u2 <= 1:
            return True
        else:
            return False

def create_line_from_individual(individual, task):
    angle = math.radians(individual[0])
    tan = math.tan(angle)

    y = tan * task.X + individual[1][1]
    return [individual[1],(task.X,y)]