from itertools import permutations

with open("input.txt", "r") as f:
    raw_data = f.readlines()

data = []
for line in raw_data:
    segment, message = line.split("|")
    data.append((segment.strip(), message.strip()))


def print_display(message, arrangement):
    print("--------------")
    number_strings = []

    for num in message.split(" "):
        number_string = []
        number_string.append(
            f" {arrangement['top']*4 if arrangement['top'] in num else ' '*4}"
        )
        number_string.append(
            f"{arrangement['top_left'] if arrangement['top_left'] in num else ' '} "
            f"   {arrangement['top_right'] if arrangement['top_right'] in num else ' '}"
        )
        number_string.append(
            f"{arrangement['top_left'] if arrangement['top_left'] in num else ' '} "
            f"   {arrangement['top_right'] if arrangement['top_right'] in num else ' '}"
        )
        number_string.append(
            f" {arrangement['middle']*4 if arrangement['middle'] in num else ' '*4}"
        )
        number_string.append(
            f"{arrangement['bottom_left'] if arrangement['bottom_left'] in num else ' '} "
            f"   {arrangement['bottom_right'] if arrangement['bottom_right'] in num else ' '}"
        )
        number_string.append(
            f"{arrangement['bottom_left'] if arrangement['bottom_left'] in num else ' '} "
            f"   {arrangement['bottom_right'] if arrangement['bottom_right'] in num else ' '}"
        )
        number_string.append(
            f" {arrangement['bottom']*4 if arrangement['bottom'] in num else ' '*4}"
        )
        number_strings.append(number_string)
    print(f"Message: {message}")
    for i in range(len(number_strings[0])):
        for num in number_strings:
            print(f"{num[i]}\t\t", end="")
        print()


display = {
    "top": "",
    "top_left": "",
    "top_right": "",
    "middle": "",
    "bottom_left": "",
    "bottom_right": "",
    "bottom": "",
}


signal_arrangement_map = {}
segment_perms = list(permutations("abcdefg"))
pattern_count = len(data)
current_signal = 0
for signal_pattern, message in data:
    current_signal += 1
    print(f"Analysing Signal: {current_signal}/{pattern_count}")
    signal_pattern_list = signal_pattern.split(" ")
    for perm in segment_perms:
        arrangement = {key: letter for key, letter in zip(display.keys(), perm)}
        nine = six = zero = [
            pattern for pattern in signal_pattern_list if len(pattern) == 6
        ]
        # nine = six = zero = list(filter(lambda x: len(x) == 6, signal_pattern_list))
        # one = list(filter(lambda x: len(x) == 2, signal_pattern_list))[0]
        one = [pattern for pattern in signal_pattern_list if len(pattern) == 2][0]
        # five = three = two = list(filter(lambda x: len(x) == 5, signal_pattern_list))
        two = three = five = [
            pattern for pattern in signal_pattern_list if len(pattern) == 5
        ]
        # four = list(filter(lambda x: len(x) == 4, signal_pattern_list))[0]
        four = [pattern for pattern in signal_pattern_list if len(pattern) == 4][0]
        # seven = list(filter(lambda x: len(x) == 3, signal_pattern_list))[0]
        seven = [pattern for pattern in signal_pattern_list if len(pattern) == 3][0]
        # eight = list(filter(lambda x: len(x) == 7, signal_pattern_list))[0]
        eight = [pattern for pattern in signal_pattern_list if len(pattern) == 7][0]
        if (
            (
                sorted(list(one))
                == sorted([arrangement["top_right"], arrangement["bottom_right"]])
            )
            and (
                sorted(list(four))
                == sorted(
                    [
                        arrangement["top_left"],
                        arrangement["bottom_right"],
                        arrangement["middle"],
                        arrangement["top_right"],
                    ]
                )
            )
            and (
                sorted(list(seven))
                == sorted(
                    [
                        arrangement["top"],
                        arrangement["top_right"],
                        arrangement["bottom_right"],
                    ]
                )
            )
            and (
                sorted(list(eight))
                == sorted(
                    [
                        arrangement["top"],
                        arrangement["top_right"],
                        arrangement["top_left"],
                        arrangement["middle"],
                        arrangement["bottom_right"],
                        arrangement["bottom_left"],
                        arrangement["bottom"],
                    ]
                )
            )
            and (
                sorted(
                    [
                        arrangement["top"],
                        arrangement["top_right"],
                        arrangement["middle"],
                        arrangement["bottom_left"],
                        arrangement["bottom"],
                    ]
                )
                in [sorted(s) for s in two]
            )
            and (
                sorted(
                    [
                        arrangement["top"],
                        arrangement["top_right"],
                        arrangement["top_left"],
                        arrangement["bottom_left"],
                        arrangement["bottom_right"],
                        arrangement["bottom"],
                    ]
                )
                in [sorted(s) for s in zero]
            )
            and (
                sorted(
                    [
                        arrangement["top"],
                        arrangement["top_right"],
                        arrangement["middle"],
                        arrangement["bottom_right"],
                        arrangement["bottom"],
                    ]
                )
                in [sorted(s) for s in three]
            )
            and (
                sorted(
                    [
                        arrangement["top"],
                        arrangement["top_left"],
                        arrangement["middle"],
                        arrangement["bottom_right"],
                        arrangement["bottom"],
                    ]
                )
                in [sorted(s) for s in five]
            )
            and (
                sorted(
                    [
                        arrangement["top"],
                        arrangement["top_left"],
                        arrangement["middle"],
                        arrangement["bottom_right"],
                        arrangement["bottom_left"],
                        arrangement["bottom"],
                    ]
                )
                in [sorted(s) for s in six]
            )
            and (
                sorted(
                    [
                        arrangement["top"],
                        arrangement["top_left"],
                        arrangement["top_right"],
                        arrangement["middle"],
                        arrangement["bottom_right"],
                        arrangement["bottom"],
                    ]
                )
                in [sorted(s) for s in nine]
            )
        ):
            signal_arrangement_map[message] = arrangement

number_segments = {
    0: ("top", "top_left", "top_right", "bottom_left", "bottom_right", "bottom"),
    1: ("top_right", "bottom_right"),
    2: ("top", "top_right", "middle", "bottom_left", "bottom"),
    3: ("top", "top_right", "middle", "bottom_right", "bottom"),
    4: ("top_left", "top_right", "middle", "bottom_right"),
    5: ("top", "top_left", "middle", "bottom_right", "bottom"),
    6: ("top", "top_left", "middle", "bottom_left", "bottom_right", "bottom"),
    7: ("top", "top_right", "bottom_right"),
    8: (
        "top",
        "top_left",
        "top_right",
        "middle",
        "bottom_left",
        "bottom_right",
        "bottom",
    ),
    9: ("top", "top_left", "top_right", "middle", "bottom_right", "bottom"),
}

message_numbers = []
for message, arrangement in signal_arrangement_map.items():
    print_display(message, arrangement)
    number_str = ""
    for message_number in message.split(" "):
        for number, segments in number_segments.items():
            segment_values = sorted([arrangement[segment] for segment in segments])
            sorted_message_number = sorted(message_number)
            if segment_values == sorted_message_number:
                number_str += str(number)
    message_numbers.append(int(number_str))

print(sum(message_numbers))
