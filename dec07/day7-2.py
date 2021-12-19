with open("input.txt", "r") as f:
    crabs = [int(i) for i in f.read().split(",")]

min_pos = min(crabs)
max_pos = max(crabs)

lowest_fuel_total = None
most_efficient_pos = None
for target_pos in range(min_pos, max_pos + 1):
    fuel_cost = 0
    for crab_pos in crabs:
        fuel_cost += (abs(crab_pos - target_pos) * (abs(crab_pos - target_pos) + 1)) / 2
    if not lowest_fuel_total or fuel_cost < lowest_fuel_total:
        lowest_fuel_total = fuel_cost
        most_efficient_pos = target_pos

print(f"Best Pos: {most_efficient_pos}")
print(f"Fuel Cost: {lowest_fuel_total}")
