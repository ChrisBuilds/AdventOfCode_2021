class BingoCard:
    def __init__(self, row_data):
        self.rows = self.make_rows(row_data)
        self.columns = self.make_columns()
        self.card_numbers = self.summarize_numbers()
        self.called_numbers_at_win = []

    def make_rows(self, row_data):
        rows = []
        for row in row_data:
            rows.append(row.replace("  ", " ").split(" "))
        return rows

    def make_columns(self):
        columns = []
        for i in range(len(self.rows[0])):
            column = []
            for row in self.rows:
                column.append(row[i])
            columns.append(column)
        return columns

    def check_for_win(self, called_numbers):
        win_condition_met = self._check_row_column(self.rows, called_numbers)
        if win_condition_met:
            return True
        win_condition_met = self._check_row_column(self.columns, called_numbers)
        return win_condition_met

    def _check_row_column(self, row_column, called_numbers):
        for line in row_column:
            line_called = True
            for num in line:
                if num not in called_numbers:
                    line_called = False
                    break
            if line_called:
                return True

    def summarize_numbers(self):
        card_numbers = []
        for row in self.rows:
            card_numbers.extend(row)
        return card_numbers

    def __str__(self):
        card = ""
        for row in self.rows:
            for num in row:
                card += num + " "
            card += "\n"
        return card


def make_bingo_cards(data):
    rows = []
    bingocards = []
    for row in data[2:]:
        if row == "":
            bingocards.append(BingoCard(rows))
            rows = []
        else:
            rows.append(row)
    bingocards.append(BingoCard(rows))
    return bingocards


with open("input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

uncalled_numbers = data[0].split(",")
called_numbers = []
bingocards = make_bingo_cards(data)
won = False
winning_cards = []
called_number_index = 0

while bingocards and called_number_index < len(uncalled_numbers):
    called_numbers.append(uncalled_numbers[called_number_index])
    for card in bingocards:
        won = card.check_for_win(called_numbers)
        if won:
            winning_card = card
            winning_card.called_numbers_at_win = called_numbers.copy()
            winning_cards.append(winning_card)
            bingocards.remove(card)
    called_number_index += 1

unmarked_numbers = [
    int(num)
    for num in winning_cards[-1].card_numbers
    if num not in winning_cards[-1].called_numbers_at_win
]

print(winning_cards[-1])
print(
    f"final: {sum(unmarked_numbers) * int(winning_cards[-1].called_numbers_at_win[-1])}"
)
