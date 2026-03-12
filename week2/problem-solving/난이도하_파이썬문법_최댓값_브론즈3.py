# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

nums = []

for i in range(9):
    nums.append(int(input()))

max = nums[0]

for j in range(len(nums)-1):
    if max < nums[j+1]:
        max = nums[j+1]

print(max)
print(nums.index(max)+1)
