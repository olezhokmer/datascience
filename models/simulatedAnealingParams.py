class SimulatedAnnealingParams:
    def __init__(self, cooling_factor, initial_temperature, stopping_temperature):
        self.cooling_factor = cooling_factor
        self.initial_temperature = initial_temperature
        self.stopping_temperature = stopping_temperature