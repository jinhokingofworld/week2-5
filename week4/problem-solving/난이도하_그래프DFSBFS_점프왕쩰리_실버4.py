# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173
N = int(input())
board = [[0] * N for _ in range(N)]

for i in range(N):
    temp2 = list(map(int, input().split()))
    for j in range(N):
        board[i][j] = temp2[j]

def R(x, y):
    if x == N-1 and y == N-1:
        return True
    
    val = board[x][y]
    if val != 0:
        if x + val < N:
            if R(x + val, y):
                return True
        if y + val < N:
            if R(x, y + val):
                return True

    return False

if R(0, 0):
    print('HaruHaru')
else:
    print('Hing')