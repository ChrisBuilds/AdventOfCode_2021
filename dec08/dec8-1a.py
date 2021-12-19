with open("input.txt", "r") as f:
    raw_data = f.readlines()

data = []
for line in raw_data:
    segment, message = line.split("|")
    data.append((segment.strip(), message.strip()))


def find_segments(signal_pattern, segments):
    for signal in signal_pattern:
        if len(signal) == 6 and not all(s in signal for s in segments[1]):
            segments[6] = signal
    return segments


special_digit_count = 0
for signal_pattern, message in data:
    signal_pattern = signal_pattern.split(" ")
    message = message.split(" ")
    segments = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
    for message_digit in message:
        if len(message_digit) in (2, 3, 4, 7):
            if len(message_digit) == 2:
                segments[1] = message_digit
                special_digit_count += 1
            elif len(message_digit) == 3:
                segments[7] = message_digit
                special_digit_count += 1
            elif len(message_digit) == 4:
                segments[4] = message_digit
                special_digit_count += 1
            elif len(message_digit) == 7:
                segments[8] = message_digit
                special_digit_count += 1
    segments = find_segments(signal_pattern, segments)
    print(segments)
print(special_digit_count)
