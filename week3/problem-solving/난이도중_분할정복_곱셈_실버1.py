# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

A, B, C = list(map(int, input().split()))
# result = pow(A, B) % C

# temp = (A % C)
# for i in range(B):
#     temp *= temp

# temp = (A - C)

# temp = pow(temp, B)

# result = temp % C

# if result < 0:
#     result += C
# print(result)

def mod(A, B, C):
    if B == 1:
        return A % C

    temp = mod(A, B//2, C)
    #홀수일 때
    if B % 2 == 1:
        return (A * temp * temp) % C
    else:
        return (temp * temp) % C
    
print(mod(A,B,C))