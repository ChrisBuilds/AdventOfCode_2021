with open("input.txt", "r") as f:
    data = [int(i) for i in f.readlines()[0].split(",")]

school = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
for d in data:
    school[d] += 1
day = 0
while day < 256:
    new_school = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for days_remaining in school:
        if days_remaining == 0:
            new_school[8] = school[0]
            new_school[6] += school[0]
        else:
            new_school[days_remaining - 1] += school[days_remaining]
    school = new_school.copy()
    day += 1
print(sum(school.values()))
