# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

number = int(input())

for i in range(number):
    result = 0
    sum = 0
    avg = 0
    count = 0

    temp = list(map(int, input().split()))
    
    for j in range(1, temp[0]+1):
        sum += temp[j]
        avg = sum / temp[0]
    
    for k in range(1, temp[0]+1):
        if temp[k] > avg:
            count += 1

    format_num = round((count / temp[0])*100, 2)
    print(str(format_num) + "%")

# 인풋을 받고 그 수만큼 반복
    # 인풋을 받고 리스트에 스플릿을 해서 저장 list(map(int, input().split()))
    # 인덱스 1부터 끝까지 서칭하여 더하고 인덱스0 으로 나누어 평균 구함
    # 다시 리스트를 돌아서 평균을 넘는 점수들을 카운팅. 분자를 구함
    # 백분율 = 분자 / 분모 * 100%
    # 소숫점 셋째 자리까지 출력