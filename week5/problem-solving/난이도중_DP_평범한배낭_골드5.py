# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

# N 물품의 수, K 무게
# N, K = map(int, input().split())
# items = []
# dp = []
# for i in range(N):
#     A, B = map(int, input().split())
#     items.append((A, B))

# items.sort(key = lambda x: (x[1]/x[0], -x[0]))
# last = items.pop()
# dp.append(last)
# print(dp)
# for i in range(len(items)):
#     current = items.pop()
#     print(current, end=" ")
#     print(last)
#     # 배낭에 무게가 남으면 일단 넣어
#     if dp[-1][0] + current[0] < K: 
#         dp.append((dp[-1][0] + current[0], dp[-1][1] + current[1]))
#         last = current
#     # 못 넣는다면 전에꺼 빼고 넣는거랑 안넣는 거랑 가치 비교
#     else:
#         if (dp[-1][0] - last[0]) != 0:
#             yesnow = (dp[-1][1] - last[1]) / (dp[-1][0] - last[0])
#         else:
#             yesnow = dp[-1][1] - last[1]
#         notnow = dp[-1][1] / dp[-1][0]
#         #지금께 크면, 지금꺼 넣어
#         if yesnow > notnow:
#             dp.append((dp[-1][0] - last[0] + current[0], dp[-1][1] - last[1] + current[1]))
#             last = current
#         #안넣는게 크면, 안넣어
#         else:
#             dp.append(dp[-1])
#     print(dp)
    
# print(dp[-1][1])

#물건 개수 N, 최대 무게 K
N, K = map(int, input().split())
items = []
dp = []
for i in range(N):
    A, B = map(int, input().split())
    items.append((A, B))

#무게순으로 정렬
items.sort(key = lambda x: (-x[0], x[1]))

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