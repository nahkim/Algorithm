w = []
k = []
wsum = 0
ksum = 0

for i in range(10):
    w.append(int(input()))
w.sort()
wsum = w[9] + w[8] + w[7]

for i in range(10):
    k.append(int(input()))
k.sort()
ksum = k[9] + k[8] + k[7]

print(wsum, ksum)