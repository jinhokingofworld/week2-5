# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639
from collections import deque
import sys

#큐에 봐야할 숫자들을 넣는다.
q = deque([])
lines = sys.tedin.readlines()
for line in lines:
    q.append(int(line))

#트리를 만들 노드를 생성
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

s = deque([])
before = None
#스택에 숫자를 확인하면서 넣어 트리를 만든다.

#루트 노드 생성
current = q.popleft()
s.append(current)
before = Node(current)

#트리 연결
while len(q) > 0:
    current = q.popleft()
    if s[-1] < current:
        while s[-1] < current:
            s.pop()
    s.append(current)
    #이전에 나온 값보다 작으면 left에 잇고, 스택 팝하고 크다면 부모노드랑 비교
    if before.val < current:

#완성된 트리를 DFS한다.

#트래킹 목록
#현재숫자
#이전숫자
#다음숫자

#트리를 어떻게 만들지?
#트리를