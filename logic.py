def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]



def other_player(player):
	if now == 'X':
              next = 'Y"
	else:
		new = 'X'
	return new


def get_winner(input_board):
	for i in range(0, 3):
		if input_board[i][0] != '' and input_board[i][0] == input_board[i][1] == input_board[i][2]:
			print(input_board[i][0], ' Won')
			return input_board[i][0]
	for i in range(0, 3):
		if input_board[0][i] != '' and input_board[0][i] == input_board[1][i] == input_board[2][i]:
			print(input_board[0][i], ' Won')
			return input_board[0][i]
	if input_board[1][1] != '' and (
			input_board[0][0] == input_board[1][1] == input_board[2][2] or input_board[2][0] == input_board[1][1] ==
			input_board[0][2]):
		print(input_board[1][1], ' Won')
		return input_board[1][1]
	for row in input_board:
		for col in row:
			if col == '':
				return ''
	print('Draw')
	return 'Draw'
