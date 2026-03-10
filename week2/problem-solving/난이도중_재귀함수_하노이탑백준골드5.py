# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

N = int(input())

def hanoi(n, start, blank, end):
    if n == 1:
        print(str(start) +" "+ str(end))
        return
    
    hanoi(n-1, start, end, blank)
    hanoi(1, start, blank, end)
    hanoi(n-1, blank, start, end)


print(2**N - 1)
if N <= 20:
    hanoi(N, 1, 2, 3)

# N개의 탑중에 N-1개를 빈 칸으로 놓음
# 밑의 한 개를 목표 칸으로 놓음
# N-1개의 탑을 목표 칸으로 놓음