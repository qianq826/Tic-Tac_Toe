from logic import make_empty_board
from logic import other_player
from logic import get_winner

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
        if board[r][c] is not None:  # Corrected this condition
            raise ValueError('input invalid, index already input')
        return r, c

if __name__ == '__main__':
  board = make_empty_board()
  winner = None
  turn = 'X'
  show_board(board)
    
  while winner == None:
     print('Next turn: ', turn)
     r, c = input_move(board)
     board[r][c] = turn
     show_board(board)
     winner = get_winner(board)
     turn = other_player(turn)
