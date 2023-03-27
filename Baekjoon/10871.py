N, X = map(int, input().split())
sequence = list(map(int, input().split()))

for i in sequence:
    if (i < X):
        print(i, end=' ')