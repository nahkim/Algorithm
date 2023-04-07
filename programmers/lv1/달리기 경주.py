def solution(players, callings):
    for name in callings:
        change = players.index(name)
        players[change - 1], players[change] = players[change], players[change - 1]
    return players