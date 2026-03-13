# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

n = int(input())
nums = list(map(int, input().split()))
used = [False] * n
best = 0

def bt(path):
    global best

    if len(path) == n:
        sum = 0
        for i in range(n-1):
            sum += abs(nums[i] - nums[i+1])
        best = max(sum, best)
        return
    
    for i in range(n):
        if used[i]:
            continue

        used[i] = True
        path.append(nums[i])

        bt(path)

        path.pop()
        used[i] = False

bt([])
print(best)




