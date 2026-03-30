# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

#물건 개수 N, 최대 무게 K
N, K = map(int, input().split())
items = []
dp = []
for i in range(N):
    A, B = map(int, input().split())
    items.append((A, B))

#무게순으로 정렬
# items.sort(key = lambda x: (-x[0], x[1]))

dt = [0] * (K+1)

#무게당 최대 효율을 내는 것
#인덱스가 해당 무게
#dt[i] = dt[]

# for i in range(items[0][0], K+1):
#     for t in items:
#         #무게가 맞다면,
#         #가치가 더 큰걸 저장
#         if i - t[0] >= 0:
#             dt[i] = max( dt[i], dt[i-t[0]]+ t[1])

for t in items:
    for i in range(K, 0, -1):
        if i - t[0] >= 0:
            dt[i] = max(dt[i], dt[i-t[0]] + t[1])

# print(dt)
print(dt[K])