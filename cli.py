from logic import make_empty_board
from logic import show_board
from logic import input_move
from logic import change_turn
from logic import get_winner


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
        turn = change_turn(turn)
