# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

# for문을 통해 B에 대해서 A에 이분탐색을 진행
import sys
n1 = int(sys.stdin.readline().strip())
temp1 = list(map(int, sys.stdin.readline().strip().split()))
temp1.sort()

n2 = int(sys.stdin.readline().strip())
temp2 = list(map(int, sys.stdin.readline().strip().split()))

#정렬되어 있어야 함
# 중간을 찾고, 타겟과 비교
# 위로 아래로 내려간 다음 찾을 때까지 반복
def b_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    mid = (left + right) // 2
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for i in temp2:
    #i를 temp1에서 binary_search
    print(b_search(temp1, i))