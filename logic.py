def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def show_board(board):
	for row in board:
		print(row)


def input_move(board):
	try:
		r = int(input("input row index: "))
		c = int(input("input col index: "))
	except:
		raise ValueError('input invalid, not int')
	else:
		if r < 0 or r > 2 or c < 0 or c > 2:
			raise ValueError('input invalid, should >=0 and <=2')
		if board[r][c] != '':
			raise ValueError('input invalid, index already input')
		return r, c
        

def change_turn(old: str):
	if old == 'X':
		new = 'Y'
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
