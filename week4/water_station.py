from agent import Agent
import utils

class WaterStation(Agent):

    def __init__(self, position):
        super().__init__(position)

    def decide(self, percept):
        for cords, value in percept.items():
            if utils.is_robot(value):
                print(value)
                return "refuel", cords, value

        return "Idle", None, None

    def act(self, environment):
        cell = self.sense(environment)
        decision, cords, value = self.decide(cell)

        if decision == "refuel":
            value.water_level = 100

    def __str__(self):
        return '💧'
