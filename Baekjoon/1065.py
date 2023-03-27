num = int(input())


# 공차 d 구하기
# 등차수열 공식
# 첫째항 a + d(n - 1)

# 숫자가 점점 커지거나, 점점 작아져야함 / 중간에 값이 커지다 작아지거나 반대일 경우 등차수열이 안됨
count = 0
if num < 100:
    count += num
else: