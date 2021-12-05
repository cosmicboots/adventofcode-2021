def check_win(board):
    rows = [set(row) for row in board]
    cols = [set(col) for col in
            [[row[i] for row in board] for i in range(len(board[0]))]]
    for row in rows:
        if len(row) == 1 and row.issubset([1]):
            return True
    for col in cols:
        if len(col) == 1 and col.issubset([1]):
            return True
    return False


def calc_score(board, checked, last_pick):
    sum = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if checked[i][j] == 0:
                sum += board[i][j]
    return sum * last_pick


def get_win_board(boards, checked):
    for board in range(len(boards)):
        if check_win(checked[board]):
            print("board", board, "won")
            return board
    return None


def ingest(input):
    """Ingest the input data"""
    input_seq = input[0]
    input.remove(input_seq)
    input_seq = [int(x) for x in input_seq.rstrip().split(",")]
    boards = []
    while input.count("\n") != 1:
        input.remove("\n")
        boards.append([[int(y) for y in x.rstrip().split()] for x in
                       input[0:input.index("\n")]])
        input = input[input.index("\n"):len(input)]
    return (input_seq, boards)


def check_spaces(boards, checked, num):
    for board in range(len(boards)):
        for row in range(len(boards[board])):
            for cell in range(len(boards[board][row])):
                if boards[board][row][cell] == num:
                    checked[board][row][cell] = 1
    return checked


def part1():
    input_seq = []
    boards = []
    with open("day04.in", "r") as f:
        input_seq, boards = ingest([line for line in f])

    checked = [[[0 for i in row] for row in board] for board in boards]
    score = 0
    for num in input_seq:
        checked = check_spaces(boards, checked, num)
        win_board = get_win_board(boards, checked)
        if win_board is not None:
            score = calc_score(boards[win_board], checked[win_board], num)
            break
    print("Winning score:", score)


def part2():
    with open("day04.in2", "r") as f:
        input_seq, boards = ingest([line for line in f])

    checked = [[[0 for i in row] for row in board] for board in boards]
    win_boards = [0 for i in range(len(boards))]
    loosing_board = -1
    for num in input_seq:
        checked = check_spaces(boards, checked, num)
        if loosing_board != -1:
            score = calc_score(boards[loosing_board], checked[loosing_board],
                               num)
            break
        for board in range(len(checked)):
            if check_win(checked[board]):
                win_boards[board] = 1
        if win_boards.count(0) == 1:
            loosing_board = win_boards.index(0)
            score = calc_score(boards[loosing_board], checked[loosing_board],
                               num)
    print("board", loosing_board, "lost")
    print("Loosing score:", score)


def main():
    print("=== PART 1 ===")
    part1()
    print("=== PART 2 ===")
    part2()


if __name__ == "__main__":
    main()
