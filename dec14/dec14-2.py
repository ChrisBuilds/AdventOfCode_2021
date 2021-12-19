from typing import OrderedDict


with open("input.txt") as f:
    data = [l.strip() for l in f.readlines()]

template = data[0]
rules = {d.split(" -> ")[0]: d.split(" -> ")[1] for d in data[2:]}
template_map = OrderedDict()
for i, polymer in enumerate(template):
    if i <= len(template) - 2:
        pair = polymer + template[i + 1]
        if pair in template_map:
            template_map[pair] += 1
        else:
            template_map[pair] = 1


def insert_pairs(template_map):
    new_template_map = OrderedDict()
    for pair, count in template_map.items():
        if count > 0:
            if pair[0] + rules[pair] in new_template_map:
                new_template_map[pair[0] + rules[pair]] += count
            else:
                new_template_map[pair[0] + rules[pair]] = count
            if rules[pair] + pair[1] in new_template_map:
                new_template_map[rules[pair] + pair[1]] += count
            else:
                new_template_map[rules[pair] + pair[1]] = count
    return new_template_map


char_count = {}
for c in data[0]:
    if c in char_count:
        char_count[c] += 1
    else:
        char_count[c] = 1
for i in range(40):
    print(f"\rInsertion Step: {i}", end="")
    for pair, count in template_map.items():
        if rules[pair] in char_count:
            char_count[rules[pair]] += count
        else:
            char_count[rules[pair]] = count
    template_map = insert_pairs(template_map)
print(char_count)
most_common = max(char_count, key=char_count.get)
least_common = min(char_count, key=char_count.get)
print(char_count[most_common] - char_count[least_common])
