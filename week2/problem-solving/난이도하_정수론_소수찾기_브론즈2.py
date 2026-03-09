# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

#문제
#주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

#입력
#첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

#Split은 리스트로 만든다.

import math
n = int(input())
nums = list(map(int, input().split()))
count = 0

for i in nums:
    if i < 2:
        continue
    prime = True

    #for문으로 반 까지 나눔
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            prime = False
    if prime:
        count += 1

print(count)