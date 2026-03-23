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
before = 0
queue = deque([0])
count = 0
seen = set({})

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