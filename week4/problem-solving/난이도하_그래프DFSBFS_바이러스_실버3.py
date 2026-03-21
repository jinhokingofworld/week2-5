# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
from collections import deque

nodes = int(input())
edges = int(input())
# 인덱스 1부터 사용하기 위함
graph = [[] for _ in range(nodes + 1)]

#인접한 노드 리스트에 표시
for _ in range(edges):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

#DFS
#stack 활용
def dfs(start: int):
    result = []

    #해시셋과 스택을 초기화
    s = deque([])
    s.append(start)
    seen = set({start})

    #인접한 것들 본 적 없으면 큐에 넣고 빼길 반복
    while len(s) > 0:
        current = s.pop()
        if current > 0:
            result.append(current)

        for i in graph[current]:
            if i not in seen:
                s.append(i)
                seen.add(i)

    return len(result)

#재귀 활용 DFS
def recursionDfs(start: int, seen, result):
    seen.add(start)
    #현재 노드 선택
    if start > 1:
        result.append(start)
    
    #다음 연결된 노드들 탐색
    for next in graph[start]:
        if next not in seen:
            recursionDfs(next, seen, result)

    return len(result)

#BFS
def bfs(start: int):
    result = []
    #해시셋과 큐를 초기화
    q = deque([])
    q.append(start)
    seen = set({start})

    #인접한 것들 본 적 없으면 큐에 넣고 빼길 반복
    while len(q) > 0:
        current = q.popleft()
        if current > 1:
            result.append(current)

        for i in graph[current]:
            if i not in seen:
                q.append(i)
                seen.add(i) 

    return len(result)

#print(dfs(1))
# print(bfs(1))
print(recursionDfs(1, set(), []))