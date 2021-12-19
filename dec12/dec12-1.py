def travel(visited, path, position, first_small, depth):
    global full_routes
    global route_count
    depth += 1
    path.append(position)
    small_cave_ignored = False
    if position not in ("start", "end") and position == position.lower():
        if not first_small:
            first_small = position
            small_cave_ignored = True
        else:
            visited.append(position)
    if position == "end":
        potential_moves = []
        if path not in full_routes:
            full_routes.append(path)
            route_count += 1
            print(f"\rDepth: {depth} Route Count: {route_count}     ", end="")

    else:
        potential_moves = [
            room for room in cave_map.get(position) if room not in visited
        ]

    while position != "end" and potential_moves:
        for move in potential_moves:
            next_position = move
            travel(visited.copy(), path.copy(), next_position, first_small, depth)
        if small_cave_ignored:
            visited.append(position)
            small_cave_ignored = False
            first_small = ""
        else:
            potential_moves = []
    return


with open("input.txt") as f:
    data = [l.strip() for l in f.readlines()]


cave_map = {}
for line in data:
    caves = line.split("-")
    if caves[0] not in cave_map.keys():
        cave_map[caves[0]] = []
    if caves[1] not in cave_map[caves[0]] and caves[1] != "start":
        cave_map[caves[0]].append(caves[1])
    if caves[1] not in cave_map.keys():
        cave_map[caves[1]] = []
    if caves[0] not in cave_map[caves[1]] and caves[0] != "start":
        cave_map[caves[1]].append(caves[0])
cave_map.pop("end", None)
full_routes = []
path = []
position = "start"
visited = []
first_small = ""
route_count = 0
depth = 1
travel(visited, path, position, first_small, depth)
