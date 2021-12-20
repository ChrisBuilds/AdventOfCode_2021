with open("input.txt") as f:
    data = [l.strip() for l in f.readlines()]


def explode_check(sn_str):
    max_depth = 0
    depth = 0
    for char in sn_str:
        if char == "[":
            depth += 1
            if depth > max_depth:
                max_depth = depth
                if max_depth == 5:
                    return True
        elif char == "]":
            depth -= 1


def split_check(sn_list):
    split_found = False
    for i in sn_list:
        if isinstance(i, list):
            split_found = split_check(i)
        elif i > 10:
            split_found = True
            return split_found
    return split_found


def explode(sn_str):
    depth = 0
    global explode_left
    global explode_right
    for i, char in enumerate(sn_str):
        if char == "[":
            depth += 1
        if depth == 5:
            explode_left, explode_right = sn_str[i + 1 : i + 4].split(",")
            left_str = sn_str[:i][::-1]
            right_str = sn_str[i + 6 :]
            break
    print()


def reduce_snail_num(sn_str, sn_list):
    pending_explode = explode_check(sn_str)
    while pending_explode:
        if pending_explode:
            explode(sn_str)

    pending_split = split_check(sn_list)


explode_left = None
explode_right = None
for snail_num in data:
    sn_str = snail_num
    sn_list = eval(snail_num)
    snail_num = reduce_snail_num(sn_str, sn_list)
