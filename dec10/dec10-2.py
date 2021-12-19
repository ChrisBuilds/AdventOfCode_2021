with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

validated_lines = []
symbol_map = {"(": ")", "[": "]", "{": "}", "<": ">"}
autocomplete_symbol_points = {")": 1, "]": 2, "}": 3, ">": 4}
completion_strings = []
for line in lines:
    corrupted = False
    expected_symbols = []
    for symbol in line:
        if symbol in symbol_map.keys():
            expected_symbols.insert(0, symbol_map[symbol])
        elif symbol in symbol_map.values():
            if symbol != expected_symbols[0]:
                corrupted = True
                break
            else:
                expected_symbols.pop(0)
    if not corrupted:
        completion_strings.append("".join(expected_symbols))

autocomplete_scores = []
for completion_string in completion_strings:
    score = 0
    for symbol in completion_string:
        score = (score * 5) + autocomplete_symbol_points[symbol]
    autocomplete_scores.append(score)
print(sorted(autocomplete_scores)[int(len(autocomplete_scores) / 2)])
