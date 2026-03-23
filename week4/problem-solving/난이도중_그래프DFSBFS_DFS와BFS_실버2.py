# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

stack = deque([V])
queue = deque([V])

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

#DFS의 순서가 작은 숫자부터 되는 것을 원하기 때문에
# seen을 표시하는 시점을 pop한 이후로 변경
def DFS():
    result = []
    seen = set({V})

    while len(stack) > 0:
        current = stack.pop()
        seen.add(current)

        if current not in result:
            result.append(current)

        graph[current].sort(reverse=True)
        for i in graph[current]:
            if i not in seen:
                stack.append(i)
        
    for r in result:
        print(r, end=" ")

#BFS는 큐에 넣을 때 seen처리하는게 정석
def BFS():
    result2 = []
    seen2 = set({V})

    while len(queue) > 0:
        current = queue.popleft()
        result2.append(current)

        graph[current].sort()
        for i in graph[current]:
            if i not in seen2:
                queue.append(i)
                seen2.add(i)

    for r in result2:
        print(r, end=" ")

DFS()
print()
BFS()
