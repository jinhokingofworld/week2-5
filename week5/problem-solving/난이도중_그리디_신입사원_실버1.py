# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

# 1차 서류시험, 2차 면접시험
#적어도 하나가 다른 지원자보다 떨어지지 않는 사람만 선발

#서류점수나 면접 점수가 최댓값을 가져야 함
import sys
input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase):
    N = int(input())
    tempC = []
    for __ in range(N):
        #A는 서류점수, B는 면접점수
        A, B = map(int, input().split())
        tempC.append((A, B))
    
    tempC.sort(key= lambda x: x[0])

    bestB = float('inf')
    count = 0

    for i in tempC:
        if i[1] < bestB:
            bestB = i[1]
            count +=1

    print(count)