x, y = input().split()

rev_x = x[::-1]
rev_y = y[::-1]
rev_res = int(rev_x) + int(rev_y)
rev_res = str(rev_res)
print(int(rev_res[::-1]))