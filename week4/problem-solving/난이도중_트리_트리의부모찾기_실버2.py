# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725
from collections import deque
N = int(input())

queue = deque([1])
seen = set({1})
result = [0] * (N + 1)
graph = [[] for _ in range(N+1)]

for i in range(N-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

while len(queue) != 0:
    current = queue.popleft()
    for i in graph[current]:
        if result[i] == 0:
            result[i] = current
        if i not in seen:
            queue.append(i)
            seen.add(i)

for i in range(2, len(result)):
    print(result[i])