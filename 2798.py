def black_jack(n, m, cards):
    total = 0
    max_total = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                total = cards[i] + cards[j] + cards[k]
                if total <= m and total > max_total:
                    max_total = total
                    if max_total == m:
                        return max_total
    return max_total

n, m = map(int, input().split())
cards = list(map(int, input().split()))
print(black_jack(n, m, cards))