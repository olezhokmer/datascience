from models.geneticAlgorithmParams import GeneticAlgorithmParams
from models.simulatedAnealingParams import SimulatedAnnealingParams
from models.taskModel import TaskModel

geneticAlgorithmParams = GeneticAlgorithmParams(10, 30, 0.05)
simulatedAnnealingParams = SimulatedAnnealingParams(0.99, 50, 0.1)
taskModel = TaskModel(12, 15, [
    [(3, 6), (3, 8), (5, 8), (7, 6)],
    [(1, 2), (2, 3), (3, 2), (2, 1)],
    [(4, 4), (6, 5), (6, 4), (5, 3)],
    [(8, 2), (9, 4), (12, 7), (11, 4)]
])

tasks = [taskModel ]


    

