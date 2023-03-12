import sys

s_list = sys.stdin.readline().strip().split(":")
res = ""
check = True

for s in s_list:
    if s == "":
        if check:
            for i in range(8 - len(s_list) + 1):
                res += "0000:"
            check = False
        else:
            res += "0000:"
    else:
        if len(s) != 4:
            for i in range(4 - len(s)):
                res += "0"
        res += s + ":"
print(res[:-1])