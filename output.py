def parse_individual_to_equation(individual):
    angle = math.radians(individual[0])
    tan = math.tan(angle)

    return "Кут " + str(individual[0]) + "; Точка початку руху (" + str(individual[1][0]) + ", " + str(individual[1][1]) + "); Перетиняє " + str(calculate_fitness_for_individual(individual)) + " об'єкти."

def print_steps(population):
    lists = list(map(lambda x: parse_individual_to_equation(x), population))
    for eq in lists:
        print(eq)
    print('-------------------------------------------------------------------------')