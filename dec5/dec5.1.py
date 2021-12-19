with open("input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

# ((x1,y1), (x2,y2))


def parse_coord_line(coord_line):
    coords1, coords2 = coord_line.split(" -> ")
    x1, y1 = coords1.split(",")
    x2, y2 = coords2.split(",")
    return ((int(x1), int(y1)), (int(x2), int(y2)))


def get_delta(coords):
    num1, num2 = coords
    try:
        delta = (num1 - num2) / abs(num1 - num2)
    except ZeroDivisionError:
        return 0
    return delta


def find_all_points(line_segment):
    x1 = line_segment[0][0]
    y1 = line_segment[0][1]
    x2 = line_segment[1][0]
    y2 = line_segment[1][1]
    x_delta = int(get_delta((x2, x1)))
    y_delta = int(get_delta((y2, y1)))
    points = []
    if (x1 == x2) or (y1 == y2):
        while (x1, y1) != (x2, y2):
            points.append((x1, y1))
            x1 += x_delta
            y1 += y_delta
        points.append((x1, y1))

    return points


all_points = {}
for l in data:
    coords = parse_coord_line(l)
    points = find_all_points(coords)
    for point in points:
        if point in all_points:
            all_points[point] += 1
        else:
            all_points[point] = 1
print(len([p for p in all_points if all_points[p] > 1]))
