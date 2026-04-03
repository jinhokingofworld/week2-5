# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251

s1 = list(input())
s2 = list(input())

#문자열의 길이
x = len(s1)
y = len(s2)

#문자길이가 6이라면 인덱스0~6까지 저장
dt = [[-1 for _ in range(y+1)] for _ in range(x+1)]

def LCS(i, j):
    #base case
    if i == 0 or j == 0:
        return 0

    #dt에 값이 있다면 바로 리턴
    if dt[i][j] != -1:
        return dt[i][j]

    #맨 끝 값이 같다면
    if s1[i-1] == s2[j-1]:
        dt[i][j] = LCS(i-1, j-1) + 1

    #맨 끝 값이 다르다면
    if s1[i-1] != s2[j-1]:
        dt[i][j] = max(LCS(i-1, j), LCS(i, j-1))

    return dt[i][j]

print(LCS(x, y))