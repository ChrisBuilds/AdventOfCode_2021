def get_height_at_coord(coord):
    x, y = coord
    height = 10
    if x in range(len(heightmap[0])) and y in range(len(heightmap)):
        height = heightmap[y][x]
    return height


def get_adjacent(coord):
    x, y = coord
    adjacent_coords = [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]
    adjacent_heights = [get_height_at_coord(coord) for coord in adjacent_coords]
    return adjacent_heights


with open("input.txt") as f:
    data = [list(l.strip()) for l in f.readlines()]

heightmap = [list(map(int, l)) for l in data]
low_points = []
for y in range(len(heightmap)):
    for x in range(len(heightmap[0])):
        if get_height_at_coord((x, y)) < min(get_adjacent((x, y))):
            low_points.append(get_height_at_coord((x, y)))

print(sum([n + 1 for n in low_points]))
