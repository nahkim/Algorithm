s = input()
find_s = input()

count = 0
i = 0
while i < len(s) - (len(find_s) - 1):
    if s[i:i + len(find_s)] == find_s:
        count += 1
        i += len(find_s)
    else:
        i += 1
print(count)