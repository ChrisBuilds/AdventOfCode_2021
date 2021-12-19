from math import prod


class Packet:
    def __init__(self, payload, depth):
        self.payload = payload
        self.literal_value = None
        self.packet_length = 0
        self.decoded_hex = payload
        self.version = self.decode_version()
        self.type = self.decode_type()
        self.depth = depth
        self.type_map = {
            0: "sum(",
            1: "prod(",
            2: "min(",
            3: "max(",
            5: "gt(",
            6: "lt(",
            7: "eq(",
        }
        if self.type == 4:
            self.literal_value = self.decode_literal()
            self.payload = self.decoded_hex[self.read_position :]
            if not self.payload.strip("0"):
                # if payload is only padding 0's, discard payload, record for length accounting
                if self.payload:
                    self.packet_length += self.payload.count("0")
                self.payload = None

        else:
            self.length_type_id = self.decode_length_type()
            if self.length_type_id == 0:
                self.sub_packets_length = self.decode_sub_packets_length()
                self.payload = self.decoded_hex[self.read_position :]
            elif self.length_type_id == 1:
                self.sub_packets_count = self.decode_sub_packets_count()
                self.payload = self.decoded_hex[self.read_position :]
        self.packet_length += self.read_position

    def decode_version(self):
        return int(self.decoded_hex[:3], 2)

    def decode_type(self):
        return int(self.decoded_hex[3:6], 2)

    def decode_literal(self):
        literal_binary = ""
        literal_bits = self.decoded_hex[6:]
        groups = [literal_bits[i : i + 5] for i in range(0, len(literal_bits), 5)]
        literals = 0
        for group in groups:
            literals += 1
            literal_binary += group[1:]
            if group[0] == "0":
                break
        self.read_position = 6 + len(literal_binary) + literals
        return int(literal_binary, 2)

    def decode_length_type(self):
        self.read_position = 7
        return int(self.decoded_hex[6])

    def decode_sub_packets_length(self):
        self.read_position = 22
        return int(self.decoded_hex[7:22], 2)

    def decode_sub_packets_count(self):
        self.read_position = 18
        return int(self.decoded_hex[7:18], 2)


operation_map = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda x: int(x[0] > x[1]),
    6: lambda x: int(x[0] < x[1]),
    7: lambda x: int(x[0] == x[1]),
}


def parse_packet(data):
    global operation
    global bits_parsed
    packet = Packet(data, bits_parsed)
    if packet.type != 4:
        operation += packet.type_map[packet.type]
    bits_parsed += packet.packet_length
    payload = packet.payload
    values = []
    # Print Details
    print("Packet Details")
    print("--------------")
    print(f"Version: {packet.version}")
    print(f"Type: {packet.type}")
    if packet.type == 4:
        print(f"Literal: {packet.literal_value}")
    else:
        print(f"Length Type: {packet.length_type_id}")
        if packet.length_type_id == 0:
            print(f"Sub-packet(s) Bits Length: {packet.sub_packets_length}")
        elif packet.length_type_id == 1:
            print(f"Sub-packet(s) Count: {packet.sub_packets_count}")
    if packet.payload:
        print(f"Payload: {packet.payload}")
    print("\n")
    #############################
    if packet.type == 4:
        operation += f"{str(packet.literal_value)},"
        return packet.literal_value, packet
    elif packet.length_type_id == 0:
        sub_packet_bits = packet.sub_packets_length
        while sub_packet_bits > 0:
            result, sub_packet = parse_packet(bits_string[bits_parsed:])
            sub_packet_bits -= bits_parsed - sub_packet.depth
            values.append(result)

    elif packet.length_type_id == 1:
        sub_packet_count = packet.sub_packets_count
        parsed_sub_packets = 0
        while parsed_sub_packets != sub_packet_count:
            result, sub_packet = parse_packet(bits_string[bits_parsed:])
            parsed_sub_packets += 1
            values.append(result)
    operation += "),"
    return operation_map[packet.type](values), packet


with open("input.txt") as f:
    data = f.read().strip()

operation = ""
bits_string = "".join(f"{bin(int(c, 16))[2:]:0>4}" for c in data)
bits_parsed = 0
result, _ = parse_packet(bits_string)
print(result)
print(operation.replace(",)", ")").strip(","))
