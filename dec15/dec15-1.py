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


def a_star():
    frame_count = 0
    grid = Grid(len(data[0]), len(data), 6, 6, gridlines=True, frame_counter_text=True)
    grid.holdresult = 3000

    for y in range(len(data)):
        for x in range(len(data[0])):
            color = (45 + (6 * int(data[y][x])), 0, 159 - (11 * int(data[y][x])))
            grid.fill_cell((x, y), fill=color)
    grid.save_frame()
    graph = Graph(data)
    frontier = PriorityQueue()
    start = (0, 0)
    target = (49, 49)
    frontier.put((0, start))
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()[1]
        grid.fill_cell(current, fill=(255, 0, 0))
        if not len(grid.frames) % 8:
            grid.save_frame()
        if current == target:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + (
                    int(3.2 * (abs(next[0] - target[0]) + abs(next[1] - target[1])))
                )
                frontier.put((priority, next))
                came_from[next] = current
        # if len(grid.frames) == 500:
        #   grid.save_animation(duration=50)

    path = []
    origin = target
    while origin != start:
        path.append(origin)
        origin = came_from[target]
        target = origin
    path.reverse()
    for cell in path:
        grid.fill_cell(cell, fill=(0, 255, 0))
        grid.save_frame()
    grid.save_animation(duration=50)
    print(f"Cost: {cost_so_far[(49,49)]}")


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


a_star()

# print(came_from)
