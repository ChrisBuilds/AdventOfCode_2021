def find_most_common_value_at_pos(data, pos):
    bit_string = "".join(l[pos] for l in data)
    return (bit_string.count("0") <= bit_string.count("1")) + (
        bit_string.count("0") == bit_string.count("1")
    )


def apply_criteria(data, criteria_str):
    for pos in range(len(data[0])):
        common_bit = criteria_str[int(find_most_common_value_at_pos(data, pos))]
        data = [l for l in data if l[pos] == common_bit]
        if len(data) == 1:
            return int(data[0], 2)


with open("input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

print(apply_criteria(data, "011") * apply_criteria(data, "100"))
