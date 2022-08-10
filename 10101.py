sum = 0
num1 = int(input())
num2 = int(input())
num3 = int(input())
sum = num1 + num2 + num3
if num1 == num2 == num3 == 60:
    print('Equilateral')
elif sum == 180:
    if num1 == num2 or num2 == num3 or num1 == num3:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')