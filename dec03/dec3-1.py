with open("input.txt", "r") as f:
    raw_data = f.readlines()
data = [l.strip() for l in raw_data]


gamma_bits = ""
epsilon_bits = ""

for pos in range(len(data[0])):
    one = 0
    zero = 0
    for bit in data:
        if bit[pos] == "0":
            zero += 1
        else:
            one += 1
    if zero > one:
        gamma_bits += "0"
    else:
        gamma_bits += "1"

for bit in gamma_bits:
    if bit == "0":
        epsilon_bits += "1"
    else:
        epsilon_bits += "0"

print(gamma_bits)
print(epsilon_bits)

print(int(gamma_bits, 2) * int(epsilon_bits, 2))
