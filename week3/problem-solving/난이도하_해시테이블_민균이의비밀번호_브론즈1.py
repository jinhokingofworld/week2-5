# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

n = int(input())
temp = []
found = False

for i in range(n):
    temp.append(input())


for i in range(n):
    #i번째를 뒤집기
    string = (temp[i])[::-1]
    if not found:
        for j in range(n):
            #있다면, 출력
            if string == temp[j]:
                num = len(temp[j])
                print(num, end=" ")
                print(temp[j][num//2] )
                found = True
    else:
        break
                
