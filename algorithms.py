

from geometry import *
from inputData import *
from plots import *

import random
import math


def calculate_fitness_for_individual(individual, task):
    line = create_line_from_individual(individual, task)
    intersect_count = count_intersections(line,task.objects)
    return intersect_count

def calculate_fitness(population, task):
    fitness_values = []

    for individual in population:
        fitness_values.append((calculate_fitness_for_individual(individual, task), individual))
    
    return fitness_values

def generate_chromosome(maxY):
    angle = random.uniform(0, 180)
    start_point = (0, random.uniform(0, maxY))
    chromosome = (angle, start_point)
    return chromosome

def generate_population(pop_size, task):
    population = []
    for _ in range(pop_size):
        population.append(generate_chromosome(task.Y))
    return population

def select_parents(population, task):
    ind1, ind2 = random.sample(population, 2)
    if calculate_fitness_for_individual(ind1, task) > calculate_fitness_for_individual(ind2, task):
        parent1 = ind1
    else:
        parent1 = ind2
    ind3, ind4 = random.sample(population, 2)
    if calculate_fitness_for_individual(ind3, task) > calculate_fitness_for_individual(ind4, task):
        parent2 = ind3
    else:
        parent2 = ind4
    return parent1, parent2

def crossover(parent1, parent2):
    angle1, point1 = parent1
    angle2, point2 = parent2

    if random.random() < 0.5:
        child_angle = angle1
    else:
        child_angle = angle2

    if random.random() < 0.5:
        child_point = point1
    else:
        child_point = point2
        
    return (child_angle, child_point)

def mutate_individual(individual, task):
    if random.random() < geneticAlgorithmParams.mutation_rate:
        return generate_chromosome(task.Y)
    else:
        return individual

def create_next_generation(population, task):
    next_generation = []
    for i in range(len(population)):
        parents = select_parents(population, task)
        child = crossover(parents[0], parents[1])
        child = mutate_individual(child, task)
        next_generation.append(child)

    return next_generation

def get_neighbor(individual, maxY):
    angle, point = individual
    new_angle = angle + random.uniform(-10, 10)
    val = point[1] + random.uniform(-1, 1)
    if val > maxY:
        val = maxY
    elif val < 0:
        val = 0

    new_point = (0, val)

    
    return (new_angle, new_point)

def accept(temperature, delta):
    if delta < 0:
        return True
    else:
        probability = math.exp(-delta / temperature)
        return random.uniform(0, 1) < probability

def find_max_intersection(arr):
    max_intersection = -1
    max_intersection_element = None
    
    for elem in arr:
        intersections = elem[0]
        if intersections > max_intersection:
            max_intersection = intersections
            max_intersection_element = elem
            
    return max_intersection_element

def genetic_get_line(task):
    population = generate_population(geneticAlgorithmParams.POPULATION_SIZE, task)


    for _ in range(geneticAlgorithmParams.ITERATIONS_COUNT):
        population = create_next_generation(population, task)

    with_fitness = calculate_fitness(population, task)
    maximal = find_max_intersection(with_fitness)

    line = create_line_from_individual(maximal[1], task)
    return line


def simulated_annealing_line(task):
    chromosome = generate_chromosome(task.Y)
    individual = simulated_annealing(chromosome, task)
    line = create_line_from_individual(individual, task)
    return line

def simulated_annealing(initial_individual, task):
    current_individual = initial_individual
    current_fitness = calculate_fitness_for_individual(current_individual, task)
    best_individual = current_individual
    best_fitness = current_fitness
    temperature = simulatedAnnealingParams.initial_temperature
    iteration = 0

    while temperature > simulatedAnnealingParams.stopping_temperature:
        neighbor_individual = get_neighbor(current_individual, task.Y)
        neighbor_fitness = calculate_fitness_for_individual(neighbor_individual, task)

        delta_fitness = neighbor_fitness - current_fitness
        if accept(temperature, delta_fitness):
            current_individual = neighbor_individual
            current_fitness = neighbor_fitness
            if current_fitness > best_fitness:
                best_individual = current_individual
                best_fitness = current_fitness

        temperature = temperature * simulatedAnnealingParams.cooling_factor
        iteration += 1

    return best_individual

for task in tasks:
    simulated_annealing_line = simulated_annealing_line(task)
    draw_result(task, simulated_annealing_line)
    genetic_line = genetic_get_line(task)