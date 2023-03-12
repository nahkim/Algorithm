import sys

s_list = sys.stdin.readline().strip().split(":")
res = ""

for s in s_list:
    if s == "":
        res += "0000:"
    else:
        if len(s) != 4:
            for i in range(4 - len(s)):
                res += "0"
            res += s
        else:
            res += s
        res += ":"
        
print(res)