# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

n, m = map(int, input().split())

for i in range(1, m+1):
    print(f'0 {i}')
for i in range(m, n-1):
    print(f'{i} {i+1}')