# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

seen = set()

def DFS(start):
    stack = [start]
    seen.add(start)

    while stack:
        current = stack.pop()

        for i in graph[current]:
            if i not in seen:
                stack.append(i)
                seen.add(i)

count = 0

for i in range(1, N+1):
    if i not in seen:
        DFS(i)
        count += 1

print(count)