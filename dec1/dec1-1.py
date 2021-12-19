with open("input.txt", "r") as raw_data:
    data = [int(n.strip()) for n in raw_data.readlines()]

increases = 0
for i, n in enumerate(data):
    if i > 0:
        if n > data[i - 1]:
            increases += 1

print(increases)
