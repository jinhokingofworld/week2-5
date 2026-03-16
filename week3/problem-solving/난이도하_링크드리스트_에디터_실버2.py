# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None

class LinkedList:
    def __init__(self):
        self.head = None

    #이전 노드 삭제후 다음 노드를 연결

    #이전 노드와 다음 노드 사이에 새 노드 추가

    #