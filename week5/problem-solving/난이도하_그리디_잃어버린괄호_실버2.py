# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

temp1 = input().split("-")
for j in range(len(temp1)):
    templist = map(int, temp1[j].split("+"))
    tempsum = 0
    for i in templist:
        tempsum += i
    temp1[j] = tempsum

result = temp1[0]
for i in range(1, len(temp1)):
    result -= temp1[i]
print(result)
    