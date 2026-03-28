# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

import sys
# from collections import deque
input = sys.stdin.readline

n, money = map(int, input().split())
coins = [ int(input()) for _ in range(n)]
# print(coins)
result = 0

for c in range(len(coins)):
    c = coins.pop()
    current = 0
    if money < c:
        continue

    if money >= c:
        temp = money // c
        money = money % c
        result += temp
        # print(c)
    # result += current

    if money == 0:
        break

print(result)
