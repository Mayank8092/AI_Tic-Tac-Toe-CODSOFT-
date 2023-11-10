import _random
board = [' ' for _ in range(9)]
human = 'X'
ai = 'O'
def print_board(board):
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print(' | '.join(row))
        print('-' * 9)
def available_moves(board):
    return [i for i, x in enumerate(board) if x == ' ']
def game_over(board):
    return any(winning(board, player) for player in [human, ai]) or ' ' not in board
def winning(board, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_combinations)

def minimax(board, depth, is_maximizing, alpha, beta):
    if winning(board, ai):
        return 1
    if winning(board, human):
        return -1
    if not any(x == ' ' for x in board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for move in available_moves(board):
            board[move] = ai
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in available_moves(board):
            board[move] = human
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
def ai_move():
    best_score = -float('inf')
    best_move = None
    for move in available_moves(board):
        board[move] = ai
        score = minimax(board, 0, False, -float('inf'), float('inf'))
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move
def human_move():
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move in available_moves(board):
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
while True:
    print_board(board)

    if not available_moves(board):
        print("It's a tie!")
        break

    human_turn = True
    if human_turn:
        move = human_move()
        symbol = human
    else:
        move = ai_move()
        symbol = ai

    board[move] = symbol

    if winning(board, symbol):
        print_board(board)
        if symbol == human:
            print("You win!")
        else:
            print("AI wins!")
        break

    human_turn = not human_turn
