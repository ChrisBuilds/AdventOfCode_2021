import visualaid


def draw_grid(target_area, probe_paths, failed_paths):
    x_offsets = []
    y_offsets = []
    for path in probe_paths:
        x_adjust, y_adjust = visualaid.align_coords(path)
        x_offsets.append(x_adjust)
        y_offsets.append(y_adjust)
    x_adjust, y_adjust = visualaid.align_coords(target_area)
    x_offsets.append(x_adjust)
    y_offsets.append(y_adjust)
    x_adjust = max(x_offsets)
    y_adjust = max(y_offsets)
    grid_width = 250
    grid_height = 400
    grid = visualaid.Grid(
        grid_width, grid_height, 2, 2, gridlines=False, flip_vertical=True
    )
    for x in range(grid_width):
        for y in range(grid_height):
            grid.fill_cell((x, y), fill=(0, int(0.35 * y), 160))
    for cell in target_area:
        grid.fill_cell(((cell[0] + x_adjust), (cell[1] + y_adjust)), fill=(150, 0, 0))
    for i, path in enumerate(failed_paths):
        for cell in path:
            if cell[0] < grid_width and cell[1] < grid_height:
                adjusted_cell = (cell[0] + x_adjust, cell[1] + y_adjust)
                grid.fill_cell(adjusted_cell, fill=(240, 215, 0))
                if not i % 40:
                    grid.save_frame()
        for cell in path:
            if cell in target_area:
                grid.fill_cell(
                    ((cell[0] + x_adjust), (cell[1] + y_adjust)), fill=(150, 0, 0)
                )
            else:
                grid.fill_cell(
                    ((cell[0] + x_adjust), (cell[1] + y_adjust)),
                    fill=(165, 150, 0),
                )
        grid.save_frame()
    # Clean grid
    for x in range(grid_width):
        for y in range(grid_height):
            grid.fill_cell((x, y), fill=(0, int(0.35 * y), 160))
    for cell in target_area:
        grid.fill_cell(((cell[0] + x_adjust), (cell[1] + y_adjust)), fill=(150, 0, 0))
    # Show good paths
    for i, path in enumerate(probe_paths):
        for cell in path:
            if cell[0] < grid_width and cell[1] < grid_height:
                adjusted_cell = (cell[0] + x_adjust, cell[1] + y_adjust)
                grid.fill_cell(adjusted_cell, fill=(0, 255, 0))
                if not i % 3:
                    grid.save_frame()
        for cell in path:
            if cell in target_area:
                grid.fill_cell(
                    ((cell[0] + x_adjust), (cell[1] + y_adjust)), fill=(150, 0, 0)
                )
            else:
                grid.fill_cell(
                    ((cell[0] + x_adjust), (cell[1] + y_adjust)),
                    fill=(0, int(0.35 * y), 160),
                )
        grid.save_frame()

    grid.holdresult = 1500
    grid.save_animation(duration=50)


with open("input.txt") as f:
    data = f.read().strip()

frame_count = 0
xmin = int(data.split(" ")[2].split("..")[0][2:])
xmax = int(data.split(" ")[2].split("..")[1].strip(","))
ymin = int(data.split(" ")[3].split("..")[0][2:])
ymax = int(data.split(" ")[3].split("..")[1])

target_area = []
for y in range(ymin, ymax + 1):
    for x in range(xmin, xmax + 1):
        target_area.append((x, y))

probe_paths = []
failed_paths = []
probe_position = (0, 0)
max_x_distance = abs(max(abs(coord[0]) for coord in target_area))
max_y_distance = abs(max(abs(coord[1]) for coord in target_area))
max_y_velocity = abs(ymin)
max_x_velocity = xmax
highest_reached = 0
initial_velocities = []
for x in range(1, max_x_velocity + 1):
    for y in range(-1 * max_y_velocity, max_y_velocity + 1):
        probe_path = [(0, 0)]
        probe_position = (0, 0)
        x_velocity = x
        y_velocity = y
        while (
            probe_position not in target_area
            and abs(probe_position[0]) <= max_x_distance
            and (abs(probe_position[1]) <= max_y_distance or probe_position[1] > 0)
        ):
            probe_position = (
                probe_position[0] + x_velocity,
                probe_position[1] + y_velocity,
            )
            probe_path.append(probe_position)
            # modify velocities
            if x_velocity < 0:
                x_velocity += 1
            elif x_velocity > 0:
                x_velocity -= 1
            y_velocity -= 1
        if probe_position in target_area:

            probe_paths.append(probe_path)
            initial_velocities.append((x, y))
            for point in probe_path:
                if point[1] > highest_reached:
                    highest_reached = point[1]
        else:
            failed_paths.append(probe_path)
draw_grid(target_area, probe_paths[:600:3], failed_paths[::150])
print(highest_reached)
print(len(initial_velocities))
