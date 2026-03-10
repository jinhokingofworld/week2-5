# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오, 단, 대문자와 소문자를 구분하지 않는다.
# 가장 많이 사용된 단어가 여러 개면 ? 반환

#단어를 입력받고, UPPERCASE로 변환
# 문자 하나씩 리스트에 넣고 문자의 크기만큼 for문을 실행
# 하나씩 이미 확인한 리스트에 있는지 확인, 있다면 인덱스를 뽑아서 temp2의 동일한 인덱스에 +1 넣음, 없다면 , seen에 append를 하고 동일한 인덱스에 +1 넣음

string = list(input().upper())
seen = []
temp2 = [] 

for s in string:
    index = 0
    
    # 확인한 리스트에 없다면 추가
    if s not in seen:
        seen.append(s)
        temp2.append(1)
    else: #있다면
        index = seen.index(s)
        temp2[index] += 1

max = max(temp2)

# temp2에 max가 2개 이상 존재한다면 --> count()
# print("?")
# 1개 존재한다면 해당 index
# print(seen[index])
if temp2.count(max) > 1:
    print("?")
else:
    index = temp2.index(max)
    print(seen[index])