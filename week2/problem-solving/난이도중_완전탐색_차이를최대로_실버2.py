# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

n = int(input())
nums = list(map(int, input().split()))
used = [False] * n
best = 0

def bt(path):
    global best

    #모두 선택되었을 때 최댓값 검색 하고, 반환
    if len(path) == n:
        sum = 0
        for i in range(n-1):
            sum += abs(path[i] - path[i+1])
        best = max(sum, best)
        return
    
    #순열 찾기
    #처음부터 끝까지 안 used가 False인 애들을 찾음
    for i in range(n):
        if used[i]:
            continue

        #선택
        used[i] = True
        path.append(nums[i])

        #탐색
        bt(path)

        #취소
        path.pop()
        used[i] = False

bt([])
print(best)