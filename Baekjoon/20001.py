# import sys

# sys.stdin = open('input.txt', 'r')
test_num = 0

while True:
	words = input()
	if words == '고무오리 디버깅 끝':
		break
	if test_num == 0 and words == '고무오리':
		test_num += 2
	elif words == '고무오리':
		test_num -= 1
	elif words == '문제':
		test_num += 1
if test_num == 0:
	print('고무오리야 사랑해')
else:
	print('힝구')
