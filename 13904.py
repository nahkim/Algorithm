import sys

# sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())

subject = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

subject.sort(key= lambda x : x[0])

deadline = subject[n - 1][0]
total = 0

while deadline > 0:
    check = -1
    max_score = 0
    for i in range(len(subject)):
        if subject[i][0] >= deadline:
            if max_score <= subject[i][1]:
                max_score = subject[i][1]
                check = i
    if check != -1:
        total += max_score
        subject.remove(subject[check])
    deadline -= 1
print(total)