from logic import make_empty_board, winning

def print_board(board):
    for x in range(3):
        for y in range(3):
            print(board[(x,y)], end=" ")
            if y < 2:
                print("|", end=" ")
        print()
        if x < 2:
            print("-"*9)

def get_user_input(board, player):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row and column separated by space): ")
            x, y = map(int, move.split())
            if board[(x,y)] == ".":
                return x, y
            else:
                print("Invalid move, cell already taken. Try again.")
        except (ValueError, KeyError):
            print("Invalid input, please enter the row and column indices (0 1 or 2) separated by space.")

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_player = "X"

    while winner is None:
        print_board(board)
        x, y = get_user_input(board, current_player)
        
        board[(x,y)] = current_player
        
        winner_status = winning(board)
        if winner_status in ["X won", "O won", "Draw"]:
            winner = current_player if "Draw" not in winner_status else None
        else:
            current_player = "O" if current_player == "X" else "X"

    print_board(board)
    if winner:
        print(f"Congratulations, Player {winner} wins!")
    else:
        print("It's a draw!")

