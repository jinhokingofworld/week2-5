# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971
import sys

n = int(sys.stdin.readline().strip())
table = []
visited = [False] * n
best = 100000000

for i in range(n):
    table.append(list(map(int, sys.stdin.readline().strip().split())))

def bt(path, cost):
    global best

    #path가 다 찼으면 path[0]으로 가는 가중치를 한번 더 더하고 리턴
    if len(path) == n:
        now = path[-1]
        first = path[0]
        #마지막 경로에서 시작으로 갈 수 없는 경우 그냥 리턴
        if table[now][first] == 0:
            return
        cost += table[now][first]
        best = min(cost, best)
        return

    for i in range(1, n):
        #갔던 곳이면 패스
        if visited[i]:
            continue
        #갈 수 없는 곳이면 패스
        if table[path[-1]][i] == 0:
            continue

        #선택
        visited[i] = True
        lastvisited = path[-1]
        cost += table[lastvisited][i]
        path.append(i)
        
        #탐색
        bt(path, cost)

        #취소
        #현재 방문한 곳이 2개 이상일 때
        if len(path) >= 2: 
            soonlastvisited = path[-2]
            wantcancle = path[-1]
            cost -= table[soonlastvisited][wantcancle]
        path.pop()
        visited[i] = False

bt([0], 0)
print(best)

# 2H31의 요정