# 재귀함수 - 재귀함수가 뭔가요? (백준 실버5)
# 문제 링크: https://www.acmicpc.net/problem/17478

goal = int(input())

question = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."

question2 = '"재귀함수가 뭔가요?"'

question3 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
question4 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
question5 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'

answer = '라고 답변하였지.'
blank = '____'


def recursion(current_depth):
    thisBlank = blank * current_depth
    
    print(thisBlank + question2)

    if goal == current_depth:
        print(blank * current_depth + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(thisBlank + answer)
        return
    
    print(thisBlank + question3)
    print(thisBlank + question4)
    print(thisBlank + question5)
    recursion(current_depth+1)
    print(thisBlank + answer)

print(question)
recursion(0)
