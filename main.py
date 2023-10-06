from inputData import *
from output import *
from plots import *
from algorithms import *
from tasks import *
from geometry import *
import time
from models.taskResult import TaskResult
from tabulate import tabulate

START_SIZE = 0
FINISH_SIZE = 0
SIZE_STEP = 0

START_TEMP = 0
FINISH_TEMP = 0
TEMP_STEP = 0

def solve_it(it):
    simulated_annealing_l, simulated_i = simulated_annealing_line(it)
    genetic_l, genetic_i = genetic_get_line(it)

    msg1 = '\nSimulated annealing algorithm (Orange) (Intersects ' + str(count_intersections(simulated_annealing_l, it.objects)) + ' objects): ' + parse_individual_to_equation(simulated_i)
    msg2 = '\nGenetic algorithm (Blue) (Intersects ' + str(count_intersections(genetic_l, it.objects)) + ' objects): ' + parse_individual_to_equation(genetic_i)
    with open('output.txt', 'w') as file:
        file.write(f'X = {it.X}\n')
        file.write(f'Y = {it.Y}\n\n')
        file.write('objects = [\n')
        for obj in it.objects:
            file.write(f'    {obj},\n')
        file.write(']')
        file.write(msg1)
        file.write(msg2)
    print(msg1)
    print(msg2)
    draw_result(it, simulated_annealing_l, genetic_l)


def start_input():
    print('1. Вирішити індивідуальну задачу.')
    print('2. Провести експерименти.')
    a = int(input("Виберіть пункт для запуску (1 або 2)."))

    if a == 1:
        print('1. Ввести данні ІЗ з консолі.')
        print('2. Згенерувати данні ІЗ випадковим чином.')
        b = int(input("Виберіть пункт для запуску (1 або 2)."))

        if b == 1:
            it = get_individual_task()
            solve_it(it)
        else:
            it = gen_individual_task()
            solve_it(it)
            
    else:
        result = science_params()

        global START_SIZE
        START_SIZE = result[0][0]
        global FINISH_SIZE
        FINISH_SIZE = result[0][1]
        global SIZE_STEP
        SIZE_STEP = result[0][2]

        global START_TEMP
        START_TEMP = result[1][0]
        global FINISH_TEMP
        FINISH_TEMP = result[1][1]
        global TEMP_STEP
        TEMP_STEP = result[1][2]

        geneticAlgorithmParams.POPULATION_SIZE = START_SIZE
        simulatedAnnealingParams.initial_temperature = START_TEMP

        tasks = get_data()
        print('Запускаємо генетичний алгоритм')
        gr = run_g_algorithms(tasks)
        print('Запускаємо алгоритм імітації відпалу')
        sr = run_s_algorithms(tasks)

        print('Список довжин популяції генетичного алгоритму: ' + '; '.join(str(g[0]) for g in gr))
        print('Список початкових температур алгоритму імітації відпалу: ' + '; '.join(str(s[0]) for s in sr))

        siz = int(input('Введіть довжину популяції генетичного алгоритму з якою бажаєте проводити експерименти: '))
        tem = int(input('Введіть початкову температуру алгоритму імітації відпалу з якою бажаєте проводити експерименти: '))

        gen = []
        for g in gr:
            if g[0] == siz:
                gen = g[1]

        sim = []
        for s in sr:
            if s[0] == tem:
                sim = s[1]

        data = []

        for g in gen:
            r = list(filter(lambda s: s.objLen == g.objLen, sim))[0]

            ac = 'генетичний'
            if r.fitness > g.fitness:
                ac = 'відпалу'

            t = 'генетичний'
            if r.time < g.time:
                t = 'відпалу'
            
            data.append([r.objLen, ac, t])

        headers = ["Обєктів", "Точність більша", "Час менший"]

        print(tabulate(data, headers=headers, tablefmt="grid"))




def run_s_algorithms(tasks):
    tempResults = []
    for currTemp in range(START_TEMP,FINISH_TEMP + 1, TEMP_STEP):
        print('Поточна температура для алгоритму імітації відпалу дорівнює ' + str(currTemp))
        simulatedAnnealingParams.initial_temperature = currTemp
        results = []
        for taskList in tasks:
            fits1 = []
            times = []
            for task in taskList:
                start_time = time.time()
                simulated_annealing_l, simulated_i = simulated_annealing_line(task)
                elapsed_time = (time.time() - start_time) * 1000
                times.append(elapsed_time)
                fit1 = count_intersections(simulated_annealing_l, task.objects)
                fits1.append(fit1)
            objs = taskList[0].objects

            
            timeGlob = sum(times) / len(times)
            fit1glob = sum(fits1) / (len(fits1) * len(objs))
            results.append(TaskResult(len(objs), fit1glob * 100, timeGlob))
            print('Кількість обєктів дорівнює ' + str(len(objs)) + '. Точність дорівнює ' + str(fit1glob * 100) + '%. Часу витрачено ' + str(timeGlob) + '.')
        tempResults.append([currTemp, results])
    return tempResults
        



def run_g_algorithms(tasks):
    genResults = []
    for currSize in range(START_SIZE,FINISH_SIZE+1, SIZE_STEP):
        print('Поточний розмір популяції дорівнює ' + str(currSize))
        geneticAlgorithmParams.POPULATION_SIZE = currSize
        results = []
        for taskList in tasks:
            fits2 = []
            times = []
            for task in taskList:
                start_time = time.time()
                genetic_l, genetic_i = genetic_get_line(task)
                elapsed_time = (time.time() - start_time) * 1000
                times.append(elapsed_time)
                fit2 = count_intersections(genetic_l, task.objects)
                fits2.append(fit2)
            objs = taskList[0].objects
            timeGlob = sum(times) / len(times)
            fit2glob = sum(fits2) / (len(fits2) * len(objs))
            results.append(TaskResult(len(objs), fit2glob * 100, timeGlob))
            print('Кількість обєктів дорівнює ' + str(len(objs)) + '. Точність дорівнює ' + str(fit2glob * 100) + '%. Часу витрачено ' + str(timeGlob) + '.')
        genResults.append([ currSize, results])
    return genResults

start_input()