# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904
from collections import deque
N = int(input())

def tiles(n):

    if n == 0 or n==1:
        return 1

    dp = deque([0] * 2)
    dp[0] = 1
    dp[1] = 1
    # print(dp)
    for _ in range(2, n+1):
        #중간 값이 너무 커져서 계속 나머지를 나누어주어야 함
        temp = (dp[0] + dp[1]) % 15746
        dp.append(temp)
        dp.popleft()
    return dp[-1]

print(tiles(N) % 15746)