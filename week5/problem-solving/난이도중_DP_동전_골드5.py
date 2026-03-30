# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084

testcase = int(input())

for _ in range(testcase):
    #코인 받기
    c =  int(input())
    coins = list(map(int, input().split()))
    target = int(input())

    dp = [0] * (target+1)
    dp[0] = 1

    # 코인 종류마다 반복
    for coin in coins:
        #해당 코인을 사용하여 만들 수 있는 종류의 수 더하기
        for money in range(coin, target + 1):
            dp[money] += dp[money - coin]
    
    print(dp[target])