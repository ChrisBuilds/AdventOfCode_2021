from GridImage import Grid


def get_height_at_coord(coord):
    y, x = coord
    height = 10
    if x in range(len(heightmap[0])) and y in range(len(heightmap)):
        height = heightmap[y][x]
    return height


def chart_basin(coord, basin):
    global frame_count
    global charted
    basin.append(coord)
    charted += 1
    x, y = coord
    height = get_height_at_coord(coord)
    adjacent_coords = [
        coord
        for coord in ((x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1))
        if coord not in basin and get_height_at_coord(coord) < 9
    ]
    for coord in adjacent_coords:
        if coord not in basin:
            height = get_height_at_coord(coord)
            grid.fill_cell(
                (coord[1], coord[0]), (0 + (height * 25), 0 + (height * 25), 225)
            )
            frame_count += 1
            if not frame_count % 7:
                grid.save_frame()
            basin = chart_basin(coord, basin)
    return basin


with open("input.txt") as f:
    data = [list(l.strip()) for l in f.readlines()]


frame_count = 1
heightmap = [list(map(int, l)) for l in data]

grid = Grid(
    len(heightmap[0]),
    len(heightmap),
    8,
    8,
    gridlines=True,
    gridline_color=(146, 105, 75),
    bg_color=(135, 100, 70),
)
grid.frame_counter_text_color = (240, 240, 240)

basins = []  # list(tuples(((x,y), (x,y))))
uncharted_coords = [
    (y, x) for y in range(len(heightmap)) for x in range(len(heightmap[0]))
]
for coord in uncharted_coords:
    height = get_height_at_coord(coord)
    color = (110 + (10 * height), 80 + (7 * height), 55 + (5 * height))
    grid.fill_cell((coord[1], coord[0]), color)
grid.save_image()
grid.save_frame()
charted = 0
for coord in uncharted_coords:
    if get_height_at_coord(coord) < 9:
        if not any(coord in basin for basin in basins):
            biggest_basins = [l for c in sorted(basins.copy(), key=len)[-3:] for l in c]
            for c in biggest_basins:
                height = get_height_at_coord(c)
                grid.fill_cell((c[1], c[0]), (225, 225, 0 + (25 * height)))
            for small_basin in [
                b for b in sorted(basins, key=len)[:-3] if b not in biggest_basins
            ]:
                for c in small_basin:
                    height = get_height_at_coord(c)
                    grid.fill_cell(
                        (c[1], c[0]), (0 + (height * 25), 0 + (height * 25), 225)
                    )
            height = get_height_at_coord(coord)
            color = (0 + (height * 25), 0 + (height * 25), 225)
            grid.fill_cell((coord[1], coord[0]), color)
            basin = []
            basins.append(chart_basin(coord, basin))
            print(f"\rCharted: {charted} / {len(uncharted_coords)}", end="")
    else:
        charted += 1

grid.save_animation()
basin_sizes = sorted([len(basin) for basin in basins])
product = 1
for basin_size in basin_sizes[-3:]:
    product *= basin_size

print(product)
