import math

def parse_individual_to_equation(individual):
    angle = math.radians(individual[0])
    tan = math.tan(angle)

    return "y = " + str(tan) + " * x + (" + str(individual[1][1]) + ")"

def print_steps(population):
    lists = list(map(lambda x: parse_individual_to_equation(x), population))
    for eq in lists:
        print(eq)
    print('-------------------------------------------------------------------------')