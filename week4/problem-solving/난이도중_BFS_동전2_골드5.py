# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294

#N개종류 동전 최소개수로 K원 만들기
#BFS는 queue를 이용

# N, K = map(int, input().split())
# coins = []
# dp = []
# count = 0

# #코인 리스트
# for _ in range(N):
#     c = int(input())
#     coins.append(c)

# #dp 테이블 초기화
# for _ in range(K+1):
#     dp.append(float("inf"))
# dp[0] = 0

# #오름차순으로 정렬
# coins.sort()

# for c in coins:
#     for i in range(c, K+1):
#     #    if i-c >= 0: -> 이건 필요가 없는게 안쪽 for문이 c부터 시작하기 때문에 i - c는 >= 0임
#         dp[i] = min(dp[i], dp[i-c] + 1)

# if dp[K] == float("inf"):
#     print(-1)
# else:
#     print(dp[K])

#---------------------------------------------------------

from collections import deque
N, K = map(int, input().split())
coins = []
before = 0 # 일반적으로는 size변수에 len(queue)로 한 사이클을 확인
queue = deque([0])
count = 0
seen = set({0})

#코인 리스트
for _ in range(N):
    c = int(input())
    coins.append(c)

while len(queue) != 0:
    current = queue.popleft()
    if current == K:
        break

    for c in coins:
        if current + c not in seen and current + c <= K:
            seen.add(current + c)
            queue.append(current + c)
    
    if before == current:
        count += 1
        if queue:
            before = queue[-1]
        else:
            count = -1

print(count)

#---------------------------------------------------------

# from collections import deque

# # N: 동전 종류 수, K: 목표 금액
# N, K = map(int, input().split())

# # 동전들 입력 받기
# coins = []
# for _ in range(N):
#     coins.append(int(input()))

# # BFS를 위한 큐
# # 큐에는 "현재까지 만든 금액"이 들어감
# queue = deque([0])

# # visited[x] = 금액 x를 이미 만든 적이 있는가?
# # BFS에서는 처음 도착한 것이 최소 횟수이므로
# # 한 번 방문한 금액은 다시 볼 필요가 없음
# visited = [False] * (K + 1)
# visited[0] = True

# # level = 사용한 동전 개수
# # 처음 0원은 동전을 하나도 안 쓴 상태이므로 0
# level = 0

# # BFS 시작
# while queue:
#     # 현재 큐에 들어 있는 원소들은 "같은 level"에 속함
#     # 즉, 지금 큐에 있는 금액들은 모두 동전을 level개 써서 만든 값들
#     size = len(queue)

#     # 현재 level에 있는 노드들을 전부 처리
#     for _ in range(size):
#         current = queue.popleft()

#         # 목표 금액에 도달하면,
#         # 지금 level이 곧 사용한 최소 동전 개수
#         if current == K:
#             print(level)
#             exit()

#         # 현재 금액에서 동전 하나씩 더해보기
#         for coin in coins:
#             nxt = current + coin

#             # 목표 금액을 넘지 않고,
#             # 아직 방문하지 않은 금액이면 큐에 추가
#             if nxt <= K and not visited[nxt]:
#                 visited[nxt] = True
#                 queue.append(nxt)

#     # 현재 level의 모든 금액을 다 처리했으므로
#     # 이제 다음 level로 넘어감
#     level += 1

# # 큐가 다 빌 때까지 K를 못 만들었다면 불가능
# print(-1)