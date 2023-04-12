s, e = map(int, input().split())
cnt = 1

while s < e:
    if e % 2 == 0:
        e /= 2
        cnt += 1
    elif e % 10 == 1:
        e //= 10
        cnt += 1
    else:
        break

if s == e:
    print(cnt)
else:
    print(-1)