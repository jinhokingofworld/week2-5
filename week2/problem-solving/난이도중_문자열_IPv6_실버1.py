# # 문자열 - IPv6 (백준 실버1)
# # 문제 링크: https://www.acmicpc.net/problem/3107

# arr = list(map(str, input().split('::')))
# z1 = "0"
# z2 = "00"
# z3 = "000"
# z4 = "0000"
# #1. len이 8이고, 각 자리가 4가 안되면, 0을 추가해서 4가 되게 만들어야 함
# #2. len이 8이 아니고, 첫자리가 ''이고, 다음자리가 ''이면 -> 8-len +1 으로 채우기
# #3. 중간에''이 있고 len이 8이 아니면 -> 8 -len +1 개 칸을 0으로 채우기

# # 1. '::'가 있는 경우 / 없는 경우 나누기
# # 2. 왼쪽 블록들, 오른쪽 블록들 분리
# # 3. 부족한 블록 수만큼 '0000' 채우기
# # 4. 전체 8블록 완성
# # 5. 각 블록을 zfill(4)
# # 6. ':'로 join

# def padding(array):
#     temp = []
#     for i in array:
#         match 4 - len(str(i)):
#             case 0:
#                 temp.append(str(i))
#             case 1:
#                 temp.append(z3 + i)
#             case 2:
#                 temp.append(z2 + i)
#             case 3:
#                 temp.append(z1 + i)
#             case 4: 
#                 temp.append(z4)
#     return temp

# # ::로 줄어든 것 없는 상태
# if len(arr) == 1:
#     arr = list(map(str, arr[0].split(':')))
#     result = padding(arr)

# # ::로 줄어든게 있는 상태
# else:
#     #처음부터 줄어든 상태
#     if arr[0] == "":
#         temp = []
#         for i in range(1, len(arr)):
#             temp.append(str(i))
#         for j in range(8 - len(arr) -1):
#             arr.append(z4)
#         arr.extend(temp)
#         result = padding(arr)

#     #중간에 줄어든 상태
#     elif arr[0] !="" and arr[1] != "":
#         temp = list(map(str, arr[1].split(':')))
#         arr = list(map(str, arr[0].split(':')))
#         for i in range (8 - (len(temp) + len(arr))):
#             arr.append(z4)
#         for j in temp:
#             arr.append(str(j))
#         result = padding(arr)

#     #뒤에 줄어든 상태
#     elif arr[1] == "":
#         arr = list(map(str, arr[0].split(':')))
#         for i in range (8 - len(arr)):
#             arr.append(z4)
#         result = padding(arr)
        
# print(":".join(result))


s = input()

# :: 없는 경우
if '::' not in s:
    parts = s.split(':')
    result = [x.zfill(4) for x in parts]

# :: 있는 경우
else:
    #split을 한 결과는 list이지만, left와 right에는 문자열이 들어감
    left, right = s.split('::')

    left_parts = left.split(':') if left else []
    right_parts = right.split(':') if right else []

    zero_count = 8 - (len(left_parts) + len(right_parts))

    parts = left_parts + ['0000'] * zero_count + right_parts
    result = [x.zfill(4) for x in parts]

print(':'.join(result))