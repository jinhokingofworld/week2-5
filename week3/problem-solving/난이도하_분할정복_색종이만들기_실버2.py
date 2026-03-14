# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

#색종이를 찾는 함수()
    #1. 색종이를 4분면으로 자르고
    #2. 각 종이가 한 색으로 채워져 있으면 종료.
    #3. 여러 색이 섞여 있으면 그 분면에 대해서 재귀
    #4. N = 1일 때 리턴
    #5. 4장이 모아졌을 때 모두 같은 색이면, 합치고, 아니면 그냥 둠

#색종이를 찾는 함수2()
    #1. 색종이가 전부 같은 색인지 확인 (모두 0이면 흰색, 모두 1이면 파란색)
    #2. 전부 같은 색이 아니면 4등분 해서 재귀호출

n = int(input())
paper = []

for i in range(n):
    temp = list(map(int, input().split()))
    paper.append(temp)

countw = 0
countb = 0

def make_paper(x, y, N):
    global countb
    global countw
    
    #같은 색인지 확인
    color = paper[y][x]
    mix = False

    #행 아래로 이동
    for col in range(y, N + y):
        if mix == True:
            break
        #같은 행 오른쪽으로 열 이동
        for row in range(x, N + x):
            if color != paper[col][row]:
                mix = True
                break

    #색 리턴
    if not mix:
        if color == 1:
            countb += 1
            return
        else:
            countw += 1
            return

    half = N // 2
    #4분면에 재귀함수 호출
    #1사분면
    make_paper(x, y, N//2)
    #2사분면
    make_paper(x, y+half, N//2)
    #3사분면
    make_paper(x+half, y, N//2)
    #4사분면
    make_paper(x+half, y+half, N//2)

make_paper(0, 0, n)
print(countw)
print(countb)