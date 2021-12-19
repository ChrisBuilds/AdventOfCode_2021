with open("input.txt", "r") as f:
    raw_data = f.readlines()

data = [l.strip().split(" ") for l in raw_data]

command_map = {"forward": 1, "down": 1, "up": -1}

horizontal_pos = 0
depth = 0

for command, value in data:
    if command == "forward":
        horizontal_pos += int(value) * command_map[command]
    else:
        depth += int(value) * command_map[command]

print(horizontal_pos * depth)
