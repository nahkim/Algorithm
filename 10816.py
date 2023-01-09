import sys

# sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())  # 상근이 숫자카드 갯수
card_list = list(map(int, sys.stdin.readline().split()))  # 상근이가 가지고 있는 숫자카드
m = int(sys.stdin.readline())  # 찾을 숫자카드 갯수
search_cards = list(map(int, sys.stdin.readline().split()))  # 찾을 숫자 카드

search_dict = {}  # 찾을 숫자 카드를 딕셔너리에 넣음
for i in search_cards:
    search_dict[i] = 0  # 0으로 초기화

for card in card_list:
    if card in search_dict:  # 찾을 숫자카드라면 딕셔너리에 + 1
        search_dict[card] += 1

for card in search_cards:
    print(search_dict[card], end=" ")  # value값 출력
