from models.geneticAlgorithmParams import GeneticAlgorithmParams
from models.simulatedAnealingParams import SimulatedAnnealingParams
from models.taskModel import TaskModel

from tasks import *

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

population_size = int(config['genetic_algorithm_params']['population_size'])
iterations_count = int(config['genetic_algorithm_params']['iterations_count'])
mutation_rate = float(config['genetic_algorithm_params']['mutation_rate'])

cooling_factor = float(config['simulated_annealing_params']['cooling_factor'])
initial_temperature = float(config['simulated_annealing_params']['initial_temperature'])
stopping_temperature = float(config['simulated_annealing_params']['stopping_temperature'])

    
P = 20



geneticAlgorithmParams = GeneticAlgorithmParams(0, iterations_count, mutation_rate)


simulatedAnnealingParams = SimulatedAnnealingParams(cooling_factor, 0, stopping_temperature)

def alg_params():
    pop_size = int(input("Введіть кількість елементів у популяції для генетичного алгоритму: "))
    start_temp = int(input("Введіть початкову температуру для алгоритму імітації відпалу: "))
    geneticAlgorithmParams.POPULATION_SIZE = pop_size
    simulatedAnnealingParams.initial_temperature = start_temp

def gen_individual_task():
    X = int(input("Введіть значення X: "))
    Y = int(input("Введіть значення Y: "))
    n = int(input("Введіть кількість чотирикутників: "))
    alg_params()
    return TaskModel( Y, X, generate_quadrilaterals(n, X, Y))

def get_individual_task():
    X = int(input("Введіть значення X: "))
    Y = int(input("Введіть значення Y: "))

    objects = []
    n = int(input("Введіть кількість чотирикутників: "))
    for i in range(n):
        coords = []
        for j in range(4):
            x = float(input(f"Введіть координату x{j+1} для {i+1}-го чотирикутника: "))
            y = float(input(f"Введіть координату y{j+1} для {i+1}-го чотирикутника: "))
            coords.append((x,y))
        objects.append(coords)

    alg_params()
    return TaskModel( Y, X, objects)

def science_params():
    START_SIZE = int(input("Початковий розмір популяції для генетичного алгоритму від 2 до 1000: "))
    FINISH_SIZE = int(input("Кінцевий розмір популяції для генетичного алгоритму від 2 до 1000:"))
    SIZE_STEP = int(input("Крок розміру популяції для генетичного алгоритму: "))

    START_TEMP = int(input("Початкова температура для алгоритму імітації відпалу від 50 до 500: "))
    FINISH_TEMP = int(input("Кінцева температура для алгоритму імітації відпалу від 50 до 500: "))
    TEMP_STEP = int(input("Крок температури для алгоритму імітації відпалу: "))

    

    return [
        [START_SIZE, FINISH_SIZE, SIZE_STEP],
        [START_TEMP, FINISH_TEMP, TEMP_STEP],
    ]

def get_data():
    X = int(input("Введіть значення X: "))
    Y = int(input("Введіть значення Y: "))
    start_objects_count = int(input("Введіть початкову кількість чотирикутників: "))
    end_objects_count = int(input("Введіть кінцеву кількість чотирикутників: "))
    step = int(input("Введіть крок зміни кількості чотирикутників: "))
    tasks = []

    for i in range(start_objects_count, end_objects_count+1, step):
        tasks2 = []
        for j in range(P):
            tasks2.append(TaskModel( Y, X, generate_quadrilaterals(i, X, Y)))
        tasks.append(tasks2)

    return tasks

































# def read_task_data():
#     Y = int(input("Enter Y: "))
#     X = int(input("Enter X: "))
#     objects = []
#     objects_count = int(input("Enter the number of objects: "))
#     for i in range(objects_count):
#         object_points = []
#         points_count = 4
#         for j in range(points_count):
#             point_x = int(input(f"Enter the x-coordinate of point {j+1} for object {i+1}: "))
#             point_y = int(input(f"Enter the y-coordinate of point {j+1} for object {i+1}: "))
#             object_points.append((point_x, point_y))
#         objects.append(object_points)
#     taskModel = tasks.append(TaskModel(Y, X, objects))




    

