sum = 0
check = 0   # 출력 유무 체크
for i in range(10):
    score = int(input())
    if sum < 100 and sum + score >= 100:
        if 100 - sum < sum + score - 100:   # 100과 가까이 있는 수 찾기, 만약 같다면 더 큰 숫자를 선택(else부분)
            print(sum)
            check = 1   # 출력 완료
        else:
            print(sum + score)
            check = 1   # 출력 완료
        break
    else:
        sum += score
if check == 0:  # 10개 값 모두 더해도 100이 안넘는 경우
    print(sum)