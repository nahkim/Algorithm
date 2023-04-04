def solution(board):
    o_count = 0
    x_count = 0
    answer = 1

    for n in board:
        o_count += n.count("O")
        x_count += n.count("X")
    
    if o_count > 5 or x_count > 4:
        return 0
    if (o_count - x_count != 0) and (o_count - x_count != 1):
        return 0
    if o_count == x_count == 0:
        return 1

    if o_count >= 3 or x_count >= 3:
# 가로
        cnt = 0
        for n in board:
            if n.count("O") == 3 or n.count("X") == 3:
                cnt += 1
        if cnt > 1:
            return 0
        
# 세로
        cnt = 0
        for i in range(len(board)):
            for j in range(len(board)):
                if board[j][i] == board[j][i] == board[j][i] == "O" or board[j][i] == board[j][i] == board[j][i] == "X":
                    cnt += 1
        if cnt > 1:
            return 0
        
# 대각선
        i = 0
        if board[i][i] == board[i + 1][i + 1] == board[i + 2][i + 2] == "O" or board[i][i] == board[i + 1][i + 1] == board[i + 2][i + 2] == "X":
            return 1
        else:
            return 0
        
        if board[i][i + 2] == board[i + 1][i + 1] == board[i + 2][i] == "O" or board[i][i + 2] == board[i + 1][i + 1] == board[i + 2][i] == "X":
            return 1
        else:
            return 0
    return 1