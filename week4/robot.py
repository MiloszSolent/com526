from agent import Agent
import utils
import random
import heapq

class Robot(Agent):

    def __init__(self, position: tuple[int, int], rows, cols):
        super().__init__(position)
        self.water_level = 100
        self.water_station_location = None
        self.map = list()

        for row in range(rows):
            self.map.append(["?"] * cols)
        self.map[position[0]][position[1]] = ' '

    def decide(self, percept: dict[tuple[int, int], ...]):
        free_cells = []

        if (self.water_level >= 5):
            for cords, value in percept.items():
                if value == ' ':
                    free_cells.append((cords, value))
                elif utils.is_flame(value) and self.water_level >= 5:
                    return "extinguish", cords, value
                elif utils.is_water_station(value) < 100 and self.water_station_location is None:
                    return "record_station", cords, value

            if free_cells:
                select = random.choice(free_cells)
                return "move", select[0], select[1]
        elif (self.water_station_location is not None):
            self.calc_path(self.position, self.water_station_location, self.map)
        else:
            pass

    def act(self, environment):
        cell = self.sense(environment)
        decision, cords, value = self.decide(cell)

        if decision == "move":
            self.move(environment, cords)
            self.map[self.position[1]][self.position[0]] = ' '
        elif decision == "extinguish":
            environment.extinguish(cords)
            self.water_level -= 5
        elif decision == "record_station":
            self.water_station_location = cords

        self.uncoverTiles(cell)

    def move(self, environment, to):
        if environment.move_to(self.position, to):
            self.position = to

    def uncoverTiles(self, percept: dict[tuple[int, int], ...]):
        for cords, value in percept.items():
            self.map[cords[1]][cords[0]] = value

        self.printMap()

    def printMap(self):
        for row in self.map:
            for col in row:
                print(col, end=" ")
            print()

    def __str__(self):
        return '🚒'

    # MANHATTAN DISTANCE FUNCTIONS
    def calc_path(self, start, goal, avoid):
        p_queue = []
        heapq.heappush(p_queue, (0, start))

        directions = {
            "right": (0, 1),
            "left": (0, -1),
            "up": (-1, 0),
            "down": (1, 0)
        }
        predecessors = {start: None}
        g_values = {start: 0}

        while len(p_queue) != 0:
            current_cell = heapq.heappop(p_queue)[1]
            if current_cell == goal:
                return self.get_path(predecessors, start, goal)
            for direction in ["up", "right", "down", "left"]:
                row_offset, col_offset = directions[direction]
                neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)

                if self.viable_move(neighbour[0], neighbour[1], avoid) and neighbour not in g_values:
                    cost = g_values[current_cell] + 1
                    g_values[neighbour] = cost
                    f_value = cost + self.calc_distance(goal, neighbour)
                    heapq.heappush(p_queue, (f_value, neighbour))
                    predecessors[neighbour] = current_cell

    def get_path(self, predecessors, start, goal):
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = predecessors[current]
        path.append(start)
        path.reverse()
        return path

    def viable_move(self, x, y, types):
        # You will need to do this one
        # Do not move in to a cell containing an obstacle (represented by 'x')
        # Do not move in to a cell containing a flame
        # Do not move in to a cell containing a water station
        # Do not move in to a cell containing a robot.
        # In fact, the only valid cells are blank ones
        # Also, do not go out of bounds.
        pass

    def calc_distance(self, point1: tuple[int, int], point2: tuple[int, int]):
        x1, y1 = point1
        x2, y2 = point2
        return abs(x1 - x2) + abs(y1 - y2)

    # END OF MANHATTAN DISTANCE FUNCTIONS
