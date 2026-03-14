# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164
from collections import deque

n = int(input())

l = []
q = deque(l)

for i in range(1, n+1):
    q.append(i)

while len(q) != 1:
    q.popleft()
    q.append(q.popleft())
    
print(q[0])