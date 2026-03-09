# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675


times = int(input())

for i in range(times):
    temp = input().split() # 3 ABC temp[0]=3 temp[1]="ABC"
    string = temp[1]
    stringList = string
    p = []
    
    for j in range(0, len(stringList)):
        for k in range(int(temp[0])):
            p.append(stringList[j])

    print(''.join(p))

