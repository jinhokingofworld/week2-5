# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748
n = int(input())

def fib(number, memo = None):
    if memo == None:
        memo = [None] * (number+1)
    
    memo[0] = 0
    memo[1] = 1

    if number == 1 or number == 0:
        return memo[number]

    for i in range(2, number+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[i]

print(fib(n))    
    