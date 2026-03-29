# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707
from collections import deque

N = int(input())

#인접리스트, 시작점으로 인접리스트 판별
def BFS(graph, start):
    #True면 Ateam, False면 Bteam
    Ateam = set({})
    Bteam = set({})
    queue = deque([start])
    Ateam.add(start)

    while queue:
        current = queue.popleft()

        #A팀이면 인접리스트가 다 B여야 함
        if current in Ateam:
            for i in graph[current]:
                if i 
        #B팀이면 인접리스트가 다 A여야 함
        if current in Bteam:

    
    


for _ in range(N):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    BFS(graph, 1)
