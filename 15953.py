
def first_prize(score):
    prize = 0
    if score == 0:
        return prize
    if score == 1:
        prize = 5000000
    elif score <= 1 + 2:
        prize = 3000000
    elif score <= 1 + 2 + 3:
        prize = 2000000
    elif score <= 1 + 2 + 3 + 4:
        prize = 500000
    elif score <= 1 + 2 + 3 + 4 + 5:
        prize = 300000
    elif score <= 1 + 2 + 3 + 4 + 5 + 6:
        prize = 100000
    return prize

def second_prize(score):
    prize = 0
    if score == 0:
        return prize
    if score == 1:
        prize = 5120000
    elif score <= 1 + 2:
        prize = 2560000
    elif score <= 1 + 2 + 4:
        prize = 1280000
    elif score <= 1 + 2 + 4 + 8:
        prize = 640000
    elif score <= 1 + 2 + 4 + 8 + 16:
        prize = 320000
    return prize

T = int(input())

for test_case in range(T):
    first_res_prize = 0
    second_res_prize = 0
    first, second = map(int, input().split())
    first_res_prize = first_prize(first)
    second_res_prize = second_prize(second)
    print(first_res_prize + second_res_prize)