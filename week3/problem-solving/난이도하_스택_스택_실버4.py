# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

import sys

n = int(sys.stdin.readline())

stack = []

for i in range(n):
    arr = list((sys.stdin.readline()).split())
    
    match arr[0]:
        case 'push':
            stack.append(arr[1])            
        case 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        case 'size':
            print(len(stack))
        case 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        case 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])