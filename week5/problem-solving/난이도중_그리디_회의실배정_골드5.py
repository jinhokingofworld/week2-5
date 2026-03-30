# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931
# 제일 빨리 끝나고,

N = int(input())
temp = []
for i in range(N):
    A, B = map(int, input().split())
    temp.append((A, B))
# 람다에서 내림차순은 -로 함
temp.sort(key = lambda x: (x[1], x[0]))
result = [temp.pop(0)]

for t in temp:
    #회의 시작 시간이 이전 회의 끝나는 시간보다 빠르면 패스
    if result[-1][1] > t[0]:
        continue
    else:
        result.append(t)

print(len(result))