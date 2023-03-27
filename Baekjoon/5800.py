T = int(input())

for class_ in range(1, T + 1):
    class_x = list(map(int, input().split()))
    class_x.remove(class_x[0])
    class_x.sort(reverse=True)
    max_gap = 0
    for i in range(len(class_x) - 1):
        if class_x[i] - class_x[i + 1] > max_gap:
            max_gap = class_x[i] - class_x[i + 1]
    print(f'Class {class_}')
    print(f'Max {max(class_x)}, Min {min(class_x)}, Largest gap {max_gap}')