import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def draw_result(task, line1, line2):
    fig, ax = plt.subplots()

    for obj in task.objects:
        ax.add_patch(Polygon(obj, closed=True, facecolor='red'))
    ax.plot((line1[0][0], line1[1][0]), (line1[0][1], line1[1][1]), marker='o', color='orange',  label='Simulated annealing')
    ax.plot((line2[0][0], line2[1][0]), (line2[0][1], line2[1][1]), marker='o', color='blue', label='Genetic algorithm')
    plt.xlim(0, task.X)
    plt.ylim(0, task.Y)
    plt.show()

def draw_results(results):
    
    for i in range(len(results)):
        result = results[i]

        task = result[0]
        line1 = result[1]
        line2 = result[2]

        fig = plt.figure()
        ax = fig.add_subplot(111)
        for obj in task.objects:
            ax.add_patch(Polygon(obj, closed=True, facecolor='red'))

        ax.plot((line1[0][0], line1[1][0]), (line1[0][1], line1[1][1]), marker='o', color='orange',  label='Simulated annealing')
        ax.plot((line2[0][0], line2[1][0]), (line2[0][1], line2[1][1]), marker='o', color='blue', label='Genetic algorithm')

    plt.xlim(0, results[0][0].X)
    plt.ylim(0, results[0][0].Y)
    plt.show()


