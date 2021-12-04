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


def part1():
    with open("day04.in", "r") as f:
        input_seq = [int(x) for x in f.readline().rstrip().split(",")]
        f.readline()
        boards = []
        line = f.readline()
        while line != "EOF\n":
            board = []
            while line != "\n":
                board.append([int(x) for x in line.rstrip().split()])
                line = f.readline()
            boards.append(board)
            line = f.readline()

        checked = [[[0 for i in row] for row in board] for board in boards]
        score = 0
        for num in input_seq:
            for board in range(len(boards)):
                for row in range(len(boards[board])):
                    for cell in range(len(boards[board][row])):
                        if boards[board][row][cell] == num:
                            checked[board][row][cell] = 1
            win_board = get_win_board(boards, checked)
            if win_board is not None:
                score = calc_score(boards[win_board], checked[win_board], num)
                break
        print("Winning score:", score)


def main():
    print("=== PART 1 ===")
    part1()


if __name__ == "__main__":
    main()
