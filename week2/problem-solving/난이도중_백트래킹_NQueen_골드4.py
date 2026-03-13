# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

n = int(input())
# pos = [0] * n
count = 0
used_col = [False] * n
used_diag1 = [False] * 2 * n
used_diag2 = [False] * 2 * n

# pos[row] = col
#    행   열
def backtracking (row):
    global count

    #마지막 행에 도착하면
    if row == n:
        count += 1
        return

    #어떤 열에 놓을까?
    for col in range(n):
        #현재 놓을 자리가 이전의 퀸에 간섭받지 않는 것을 확인
        #같은 열에 있는가?
        if used_col[col]:
            continue
        #대각선에 있는가?
        if used_diag1[row - col + n] or used_diag2[row + col]:
            continue
        
        #선택
        used_col[col] = True
        used_diag1[row - col + n] = True
        used_diag2[row + col] = True
        
        #탐색
        backtracking(row+1)
        
        #취소
        used_col[col] = False
        used_diag1[row - col + n] = False
        used_diag2[row + col] = False    

backtracking(0)
print(count)


# def backtracking (index, curr):
#     global count

#     if index == n:
#         count += 1
#         return

#     for j in range(n):
#         #현재 놓을 자리가 이전의 퀸에 간섭받지 않는 것을 확인
#         canQueen = True
#         for k in range(len(curr)):
#             #같은 열에 있는가?
#             if j == curr[k]:
#                 canQueen = False
#                 break
#             #대각선에 있는가?
#             if abs(j - curr[k]) == abs(index - k):
#                 canQueen = False
#                 break
        
#         if canQueen:
#             #선택
#             curr.append(j)
#             #탐색
#             backtracking(index+1, curr)
#             #취소
#             curr.pop()