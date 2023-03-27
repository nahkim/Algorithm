a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_score = 0
b_score = 0
same_win = 'same'
for i in range(10):
    if a[i] > b[i]:
        a_score += 3
        same_win = 'A'
    elif a[i] == b[i]:
        a_score += 1
        b_score += 1
    else:
        b_score += 3
        same_win = 'B'
print(a_score, b_score)
if a_score > b_score:
    print('A')
elif a_score == b_score:
    if same_win == 'same':
        print('D')
    else:
        print(same_win)
else:
    print('B')