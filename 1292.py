first, last = map(int, input().split())

sequence = []
for i in range(1, last + 1):
    for j in range(1, i + 1):
        sequence.append(i)
# print(sequence)
sum = 0
for i in range(first, last + 1):
    sum += sequence[i - 1]
print(sum)