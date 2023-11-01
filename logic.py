def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]



def other_player(player):
    if player == 'X':
        return 'Y'
    else:
        return 'X'

def get_winner(input_board):
    for i in range(0, 3):
        if input_board[i][0] is not None and input_board[i][0] == input_board[i][1] == input_board[i][2]:
            print(input_board[i][0], 'Won')
            return input_board[i][0]

    for i in range(0, 3):
        if input_board[0][i] is not None and input_board[0][i] == input_board[1][i] == input_board[2][i]:
            print(input_board[0][i], 'Won')
            return input_board[0][i]

    if input_board[1][1] is not None:
        if input_board[0][0] == input_board[1][1] == input_board[2][2] or \
                input_board[2][0] == input_board[1][1] == input_board[0][2]:
            print(input_board[1][1], 'Won')
            return input_board[1][1]

    for row in input_board:
        for cell in row:
            if cell is None:  # Checking for None as an empty cell
                return None

    print('Draw')
    return 'Draw'

