# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470
n = int(input())
sets = list(map(int, input().split()))
sets.sort()

result = []
recorde = float('inf')

def find(arr, index):
    global result
    global recorde

    target = arr[index]
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < -target:
            left = mid + 1
        else:
            right = mid -1 
    # 종료 상태는 항상 right < left
    
    for candidate in [left, right]:
        if 0 <= candidate < len(arr) and candidate != index:
            current_recorde = abs(arr[candidate] + target)
            if current_recorde < recorde:
                result = [arr[candidate], target]

for i in range(n):
    find(sets, i)
result.sort()
print(" ".join(map(str, result)))
