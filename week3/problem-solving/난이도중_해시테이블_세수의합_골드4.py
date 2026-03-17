# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

n = int(input())
sets = []
done = False

for i in range(n):
    sets.append(int(input()))
pool = set()

for i in range(n):
    for j in range(n):
        pool.add(sets[i] + sets[j])

sets.sort()
list(pool).sort()

for i in range(n-1, -1, -1):
    for j in range(n):
        if (sets[i] - sets[j]) in pool:
            print(sets[i])
            done = True
            break
    if done:
        break
