def solution(board):
    o_count = 0
    x_count = 0

    for n in board:
        o_count += n.count("O")
        x_count += n.count("X")
    
    if (o_count - x_count != 0) and (o_count - x_count != 1):
        return 0

# 가로
    x_win = 0
    o_win = 0
    for n in board:
        if n.count("O") == 3:
            o_win += 1
        if n.count("X") == 3:
            x_win += 1

# 세로
    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i] == "O":
            o_win += 1
        if board[0][i] == board[1][i] == board[2][i] == "X":
            x_win += 1

# 대각선
    if board[0][0] == board[1][1] == board[2][2] == 'O':
        o_win += 1
    elif board[0][0] == board[1][1] == board[2][2] == 'X':
        x_win += 1
    
    if board[0][2] == board[1][1] == board[2][0] == 'O':
        o_win += 1
    elif board[0][2] == board[1][1] == board[2][0] == 'X':
        x_win += 1
            
    # if x_win and o_win:
    #     return 0
    if o_win == 1 and o_count - x_count != 1:
        return 0
    if x_win == 1 and o_count - x_count != 0:
        return 0
    return 1