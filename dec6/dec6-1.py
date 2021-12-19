with open("input.txt", "r") as f:
    school = [int(i) for i in f.readlines()[0].split(",")]

day = 0
while day < 80:
    new_school = []
    for fish in school:
        if fish == 0:
            new_school.extend([6, 8])
        else:
            new_school.append(fish - 1)
    school = new_school.copy()
    day += 1
print(len(school))
