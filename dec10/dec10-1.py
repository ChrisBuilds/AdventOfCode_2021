with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

validated_lines = []
symbol_map = {"(": ")", "[": "]", "{": "}", "<": ">"}
illegal_symbols = []
for line in lines:
    corrupted = False
    expected_symbols = []
    for symbol in line:
        if symbol in symbol_map.keys():
            expected_symbols.insert(0, symbol_map[symbol])
        elif symbol in symbol_map.values():
            if symbol != expected_symbols[0]:
                corrupted = True
                illegal_symbols.append(symbol)
                break
            else:
                expected_symbols.pop(0)
    if not corrupted:
        validated_lines.append(line)
illegal_symbol_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
error_score = 0
for symbol in illegal_symbols:
    error_score += illegal_symbol_points[symbol]
print(error_score)
