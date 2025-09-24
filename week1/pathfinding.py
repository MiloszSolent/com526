import utils
import heapq

from week1 import tui


def a_star(maze, start, goal):
    # Create an empty list that will act as our priority queue
    priority_queue = list()
    heapq.heappush(priority_queue, (0, start))
    # Using heapq.heappush - add the starting node to the queue with a priority of 0

    # Providing some code for you as they will be helpful shortly
    directions = {
        "right": (0, 1),
        "left": (0, -1),
        "up": (-1, 0),
        "down": (1, 0)
    }
    predecessors = {start: None}    # Enables the get_path function to backtrack
    g_values = {start: 0}   # The g score for each cell

    # loop through the queue, this is an infinite loop that will only stop if the queue is empty
    while priority_queue:
        current_cell = heapq.heappop(priority_queue) # get this from the priority queue

        # Check if the current cell is the goal:
            # if it is, run this command:
            # return get_path(predecessors, start, goal)
        if current_cell[1] == goal:
            return get_path(predecessors, start, goal)

        # Now lets look at where we can move to from the current cell.
        # For each direction do the following:
            # Figure out the coordinates of the neighbouring cell - the offsets are provided above.
            # For example, if the direction is 'up' then you would deduct 1 from the y coordinate

        for direction in directions:
            new_cell  = current_cell[1][0] + directions[direction][0], current_cell[1][1] + directions[direction][1]
            if new_cell >= (0, 0) and new_cell <= (len(maze[0]), len(maze)) and maze[new_cell[1]][new_cell[0]] != "x" and new_cell not in g_values:
                g_cost = 1 + g_values[current_cell[1]]
                h_score = utils.manhattan_distance(new_cell, goal)
                f_value = g_cost + h_score

                g_values[new_cell] = g_cost

                heapq.heappush(priority_queue, (f_value, new_cell))

                predecessors[new_cell] = current_cell[1]

                # Check that this neighbouring cell is actually a valid move.
            # An invalid move would be one that goes outside the bounds of the map.
            # A cell that contains an 'x' is also invalid.
            # It should also not consider a cell that already has a value stored in the g_values dict created above
            # If the cell is viable:
                # We need to calculate the cost of the move!
                # Our current cell and its cost should be stored in the dictionary g_values
                # Retrieve that value - add 1 to it and we have out cost for the neighbouring cell

                # Add the neighbouring cell and its cost to the g_values dictionary,
                # Where the (x, y) coordinates are the key and the cost is the value

                # Now calculate the H score.
                # In the utils.py file there is a manhatten_distance function.
                # Use this to calculate the distance between the neighbouring cell and the goal.
                # The value it returns will be the H score

                # Using that we can calculate the overall F score by adding the cost and the H score

                # Now we have its F-Score we can add this neighbouring cell (a viable move) to our priority queue
                # You should add the cell coords (x, y) to the queue and the prioirty value should be the f-score

                # Allows the get_path function to backtrack later, do not change
    return None


def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    print("Success:")
    return path


if __name__ == "__main__":
    maze_map = utils.import_maze("mazes/maze2.txt")     # Change the path as required.

    start = utils.locate(maze_map, 's')
    # Looking at the line above, do the same thing but this time, locate the goal
    goal = utils.locate(maze_map, 'g')

    # Print out the path returned by the a_star function (after you have completed it)
    tui.display_map(maze_map)

    print(a_star(maze_map, start, goal))