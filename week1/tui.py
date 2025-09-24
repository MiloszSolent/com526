import pathfinding
import utils


def display_map(maze):
    # As the name suggests, print out the 2D array as provided in 'maze'
    # Make sure it displays nicely
    for row in maze:
        for index in row:
            print(index, end=' ')
        print("")


def show_path(maze, path):
    # We are going to show the path the A* took one step at a time
    # for each coordinate provided in path:
        # print the map, showing a dash at that coordinate.
        # However, do not overwrite the start and goal, these should continue to be displayed as 's' and 'g'
    pass # DELETE THIS LINE!


if __name__ == "__main__":
    maze_map = utils.import_maze("mazes/maze1.txt")
    start = utils.locate(maze_map, 's')
    goal = utils.locate(maze_map, 'g')

    show_path(maze_map, pathfinding.a_star(maze_map, start, goal))