with open("input.txt") as f:
    data = [l.strip() for l in f.readlines()]

template = data[0]
rules = {d.split(" -> ")[0]: d.split(" -> ")[1] for d in data[2:]}


def insert_pairs(template):
    new_template = ""
    for i, polymer in enumerate(template):
        if i <= len(template) - 2:
            pair = polymer + template[i + 1]
            new_template += f"{pair[0]}{rules.get(pair,'')}"
        else:
            new_template += template[-1]
    return new_template


for i in range(40):
    print(f"\rInsertion Step: {i}", end="")
    template = insert_pairs(template)

print(len(template))
chars = [i for i in data[0]]
chars.extend([i for i in rules.values()])
chars = sorted(list(set(chars)), key=template.count)
print(chars)
for char in chars:
    print(f"{char} : {template.count(char)}")
print(
    f"{template.count(chars[-1])} - {template.count(chars[0])} ="
    f" {template.count(chars[-1]) - template.count(chars[0])}"
)
