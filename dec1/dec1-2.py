with open("input.txt", "r") as raw_data:
    data = [int(n.strip()) for n in raw_data.readlines()]

increases = 0
prev_window = []
current_window = []
for i, n in enumerate(data):
    if len(data[i:]) >= 3:
        current_window = data[i : i + 3]
        if len(prev_window) > 0:
            if sum(current_window) > sum(prev_window):
                increases += 1
        prev_window = current_window
    else:
        break

print(increases)
