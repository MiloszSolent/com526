import math


def import_maze(file_path):
    maze = []
    try:
        with open(file_path) as f:
            for line in f:
                row = [col.lower() for col in line.strip()]
                maze.append(row)

            # quick error check
            first_row = len(maze[0])
            for row in maze:
                if len(row) != first_row:
                    raise Exception("Maze rows are not even")
            return maze
    except FileNotFoundError:
        print(f"File not found")
    except PermissionError:
        print(f"File read permissions were denied")
    except IOError as e:
        print(f"IO error: {e}")

    return []


def locate(maze, tile):
    try:
        coords = next((i, r) for r in range(len(maze)) for i in range(len(maze[r])) if maze[r][i] == tile)
        return coords
    except StopIteration:
        raise IndexError(f"A '{tile}' indicator does not exist in the maze")


def euclidean_distance(point1:tuple[int, int], point2: tuple[int, int]):
    # quick version:
    # return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

    # More understandable:
    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt(((x1-x2)**2 + (y1-y2)**2))


def manhattan_distance(point1:tuple[int, int], point2:tuple[int, int]):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)