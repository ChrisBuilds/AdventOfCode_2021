from visualaid import Grid
from queue import Queue, PriorityQueue

with open("input.txt") as f:
    data = [l.strip() for l in f.readlines()]


class Graph:
    def __init__(self, data):
        self.data = data
        self.max_x = len(data[0]) - 1
        self.max_y = len(data) - 1

    def neighbors(self, current):
        up = (current[0], current[1] - 1)
        down = (current[0], current[1] + 1)
        left = (current[0] - 1, current[1])
        right = (current[0] + 1, current[1])
        neighbors = (up, down, left, right)
        return tuple(
            neighbor
            for neighbor in neighbors
            if (neighbor[0] >= 0 and neighbor[0] <= self.max_x)
            and (neighbor[1] >= 0 and neighbor[1] <= self.max_y)
        )

    def cost(self, next):
        return int(self.data[next[1]][next[0]])


def duplicate_cave(data):
    new_caves = []
    for row in range(0, 5):
        new_cave_row = []
        for column in range(0, 5):
            cave = []
            for line in data:
                current_row = [int(d) for d in line]
                cave.append(
                    [
                        (d + column + row) % 9 if (d + column + row) % 9 > 0 else 9
                        for d in current_row
                    ]
                )
            new_cave_row.append(cave)
        new_caves.append(new_cave_row)
    new_data = []
    for cave_row in new_caves:
        for row in range(len(cave_row[0])):
            row_string = ""
            for cave in cave_row:
                row_string += "".join(str(i) for i in cave[row])
            new_data.append(row_string)
    return new_data.copy()


def a_star(data):
    data = duplicate_cave(data)
    iterations = 0
    graph = Graph(data)
    grid = Grid(
        len(graph.data[0]),
        len(graph.data),
        1,
        1,
        gridlines=True,
        frame_counter_text=True,
    )
    grid.holdresult = 3000

    for y in range(len(data)):
        for x in range(len(data[0])):
            color = (45 + (6 * int(data[y][x])), 0, 159 - (11 * int(data[y][x])))
            grid.fill_cell((x, y), fill=color)
    grid.save_frame()
    frontier = PriorityQueue()
    start = (0, 0)
    target = (len(data[0]) - 1, len(data) - 1)
    frontier.put((0, start))
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        priority, current = frontier.get()
        grid.fill_cell(current, fill=(0, int(priority / 255) + (priority % 255), 0))
        if not iterations % 60000:
            grid.save_frame()
            pass
        if current == target:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + (
                    int(2.8 * (abs(next[0] - target[0]) + abs(next[1] - target[1])))
                )
                frontier.put((priority, next))
                came_from[next] = current
        # if len(grid.frames) == 500:
        #   grid.save_animation(duration=50)
        iterations += 1
    path_frames = 0
    path = []
    origin = target
    while origin != start:
        path.append(origin)
        origin = came_from[target]
        target = origin
    path.reverse()
    for cell in path:
        grid.fill_cell(cell, fill=grid.colors["yellow"])
        if not path_frames % 30:
            pass
            grid.save_frame()
        path_frames += 1
    grid.save_animation(filename="dec14-2 visualization.gif", duration=50)
    print(f"\nCost: {cost_so_far[(len(data[0])-1,len(data)-1)]}")
    print(iterations)


def breadth_first_early_exit():

    graph = Graph(data)
    frontier = Queue()
    start = (10, 10)
    target = (5, 25)
    frontier.put(start)
    came_from = dict()
    came_from[start] = None
    grid.fill_cell(start, fill=grid.colors["orange"])
    grid.fill_cell(target, fill=grid.colors["cyan"])
    walls = (
        ((8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5)),
        ((11, 2), (11, 3), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7)),
        (
            (5, 20),
            (6, 20),
            (7, 20),
            (8, 20),
            (9, 20),
            (10, 20),
            (11, 20),
            (12, 20),
            (13, 20),
            (14, 20),
        ),
        (
            (0, 22),
            (1, 22),
            (2, 22),
            (3, 22),
            (4, 22),
            (5, 22),
            (6, 22),
            (7, 22),
            (8, 22),
            (9, 22),
            (10, 22),
            (11, 22),
            (12, 22),
        ),
    )
    for wall in walls:
        for cell in wall:
            grid.fill_cell(cell, fill=(125, 125, 125))
    while not frontier.empty():
        current = frontier.get()
        if current == target:
            break
        if current not in (start, target):
            grid.fill_cell(current, fill=(255, 0, 0))
            grid.save_frame()
        for next in graph.neighbors(current):
            if next not in came_from and not any(next in wall for wall in walls):
                if next not in (start, target):
                    grid.fill_cell(next, fill=(0, 0, 255))
                    grid.save_frame()
                frontier.put(next)
                came_from[next] = current

    origin = None
    path = []
    while origin != start:
        origin = came_from[target]
        path.append(origin)
        target = origin
    path.reverse()

    for coord in path:
        grid.fill_cell(coord, fill=(0, 255, 0))
        grid.save_frame()
    print(path)

    grid.holdresult = 3000
    grid.save_animation(duration=50)


a_star(data)

# print(came_from)
