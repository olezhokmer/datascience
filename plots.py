import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

fig, ax = plt.subplots()

def draw_result(task, line):
    for obj in task.objects:
        ax.add_patch(Polygon(obj, closed=True, facecolor='red'))
    ax.plot((line[0][0], line[1][0]), (line[0][1], line[1][1]), marker='o')
    plt.xlim(0, task.X)
    plt.ylim(0, task.Y)
    plt.show()