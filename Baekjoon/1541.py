import sys

def plus_split(form):
    res = 0
    num_list = []
    num_list = form.split("+")
    for i in range(len(num_list)):
        res += int(num_list[i])
    return res

s = sys.stdin.readline().strip()
res = 0
form = []
form = s.split("-")

for i in range(len(form)):
    tmp = plus_split(form[i])
    if i == 0:
        res += tmp
    else:
        res -= tmp
print(res)