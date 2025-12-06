def print_board(board_cells):
    print("---------")
    for row_index in range(3):
        row_data = board_cells[row_index * 3:(row_index + 1) * 3]
        print("|", ' '.join(row_data), "|")
    print("---------")


def check_state(board_cells):
    board_matrix = [list(board_cells[row_index * 3:(row_index + 1) * 3]) for row_index in range(3)]
    lines = board_matrix + [list(col) for col in zip(*board_matrix)]
    lines.append([board_matrix[d_index][d_index] for d_index in range(3)])
    lines.append([board_matrix[d_index][2 - d_index] for d_index in range(3)])

    x_wins = any(line == ['X', 'X', 'X'] for line in lines)
    o_wins = any(line == ['O', 'O', 'O'] for line in lines)

    flat_cells = [cell for row in board_matrix for cell in row]

    if (x_wins and o_wins) or abs(flat_cells.count('X') - flat_cells.count('O')) > 1:
        return "Impossible"
    if x_wins:
        return "X wins"
    if o_wins:
        return "O wins"
    if '_' in flat_cells:
        return "Game not finished"
    return "Draw"


def make_move(board_cells):
    board_matrix = [list(board_cells[row_index * 3:(row_index + 1) * 3]) for row_index in range(3)]
    print_board(board_cells)

    while True:
        user_input = input("Enter the coordinates: ").split()

        if len(user_input) != 2 or not user_input[0].isdigit() or not user_input[1].isdigit():
            print("You should enter numbers!")
            continue

        x_coord, y_coord = map(int, user_input)

        if x_coord < 1 or x_coord > 3 or y_coord < 1 or y_coord > 3:
            print("Coordinates should be from 1 to 3!")
            continue

        if board_matrix[y_coord - 1][x_coord - 1] != '_':
            print("This cell is occupied! Choose another one!")
            continue

        board_matrix[y_coord - 1][x_coord - 1] = 'X'
        break

    updated_cells = ''.join([''.join(row) for row in board_matrix])
    print_board(updated_cells)
    print(check_state(updated_cells))


input_cells = input("Enter cells: ")
make_move(input_cells)