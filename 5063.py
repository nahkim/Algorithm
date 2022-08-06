t = int(input())

for _ in range(t):
    r, e, cost = map(int, input().split())
    if r > e - cost:
        print('do not advertise')
    elif r == e - cost:
        print('does not matter')
    else:
        print('advertise')