with open("input.txt") as f:
    data = [l.strip() for l in f.readlines()]


def explode_check(sn_str):
    max_depth = 0
    depth = 0
    for char in snail_num:
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


def reduce_snail_num(sn_str, sn_list):
    pending_explode = explode_check(sn_str)
    while pending_explode:
        if pending_explode:
            



    pending_split = split_check(sn_list)



for snail_num in data:
    sn_str = snail_num
    sn_list = eval(snail_num)
    snail_num = reduce_snail_num(sn_str, sn_list)
