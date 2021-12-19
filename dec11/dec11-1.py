from GridImage import Grid


def max_energy(octopi):
    for row in octopi:
        for octopus in row:
            if octopus > 9:
                return True
    return False


def update_energy_level_at_coord(coord, octopi):
    row = coord[0]
    col = coord[1]
    energy = octopi[row][col]
    if energy >= 9:
        octopi[row][col] = 0
    else:
        octopi[row][col] += 1
    return octopi


def get_energy_level(coord, octopi):
    row = coord[0]
    col = coord[1]
    return octopi[row][col]


def flash(coord, octopi):
    row, col = coord
    adjacent = (
        (row - 1, col),
        (row - 1, col - 1),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1),
    )
    octopi[row][col] = 0
    for coord in adjacent:
        if coord[0] in range(len(octopi)) and coord[1] in range(len(octopi[0])):
            octopi[coord[0]][coord[1]] += 1

    return octopi


def step(octopi):
    global flash_count
    global all_flash
    flashed = []
    # increase all energy by one
    for row in range(len(octopi)):
        for col in range(len(octopi[0])):
            octopi[row][col] += 1

    while max_energy(octopi):
        for row in range(len(octopi)):
            for col in range(len(octopi[0])):
                coord = (row, col)
                if get_energy_level(coord, octopi) > 9 and coord not in flashed:
                    flashed.append(coord)
                    flash_count += 1
                    octopi = flash(coord, octopi)
    if len(flashed) == len(octopi) * len(octopi[0]):
        all_flash = True
    # reset all flash octopi to 0
    for coord in flashed:
        octopi[coord[0]][coord[1]] = 0
    update_grid(grid, octopi)
    for coord in flashed:
        grid.fill_cell((coord[0], coord[1]), fill=(255, 255, 0))
    grid.save_frame()
    return octopi


def update_grid(grid, octopi):
    for row in range(len(octopi)):
        for col in range(len(octopi[0])):
            energy = octopi[col][row]
            grayscale_color = max(min(250, 0 + (energy * 25)), 0)
            color = (grayscale_color, grayscale_color, grayscale_color)
            grid.fill_cell((col, row), fill=color)


with open("input.txt") as f:
    data = [list(l.strip()) for l in f.readlines()]

octopi = [list(map(int, l)) for l in data]
octopi_coords = [(y, x) for y in range(len(octopi)) for x in range(len(octopi[0]))]
grid = Grid(len(octopi[0]), len(octopi), 25, 25, gridlines=True, bg_color=(0, 0, 0))
grid.frame_counter_text_color = (225, 225, 225)
update_grid(grid, octopi)
grid.save_frame()
flash_count = 0
all_flash = False
for i in range(10000):
    octopi = step(octopi)
    if all_flash:
        print(f"ALL FLASH ON Step: {i+1}")
        break
for i in range(20):
    grid.save_frame()

print(flash_count)

grid.save_animation(duration=100)
