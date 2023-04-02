import sys

G = int(sys.stdin.readline())

gate = [-1] * G

P = int(sys.stdin.readline())
plane = []
for i in range(P):
    plane.append(int(sys.stdin.readline()))

print(gate)
print(plane)