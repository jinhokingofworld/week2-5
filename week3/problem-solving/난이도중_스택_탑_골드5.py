# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493

#자기보다 숫자가 큰 탑이 신호를 받는 구조.
#가지보다 숫자가 작은 탑이 신호를 받으면 0

#신호를 받는 탑을 알아내는 법
# 스택을 확인함.
# 자기보다 높이가 작은 탑들은 전부 pop()
# 자기보다 높이가 큰 탑이 없으면 result에 0추가하고, 자기의 정보 스택에 넣음 (index + 1, arr[index])
# 자기보다 높이가 큰 탑이 있으면, index+1을 result에 append()
# 모든 요소에 반복

n = int(input())
sets = list(map(int, input().split()))
stack = []
result = []

def laser(index):
    #현재 탑보다 작은 탑이면 제거
    while stack and stack[-1]['high'] < sets[index]:
        stack.pop()

    #전부 pop시켜서 빈 스택일 때
    if len(stack) == 0:
        result.append(0)
    else:
        result.append(stack[-1]['space'])

    #현재 탑 삽입
    stack.append({
        'space': index + 1,
        'high' : sets[index]
    })

for i in range(len(sets)):
    laser(i)

print(' '.join(map(str, result)))