# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

seen = set()
yet = set()
for i in range(1, N+1):
    yet.add(i)

def DFS(start):
    global seen
    stack = [start]

    while stack:
        current = stack.pop()
        seen.add(current)

        for i in graph[current]:
            if i not in seen:
                stack.append(i)

#yet에서 하나 pop해서 DFS돌리고, 
#len(yet - seen) == 0인지 확인
#yet - seen에서 하나 pop해서 DFS돌리고
#yet - seen == 0인지 확인

count = 0
while True:
    diff = yet - seen
    if len(diff) == 0:
        break

    now = diff.pop()
    DFS(now)
    count += 1

print(count)