# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        #문자열 앞의 빈 노드를 가리킴
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.current = self.tail

    def back(self):
        if self.current.prev == self.head:
            return
        self.current = self.current.prev
        
    def go(self):
        if self.current == self.tail:
            return
        self.current = self.current.next
         
    def insert(self, char):
        newNode = Node(char)
        newNode.prev = self.current.prev
        newNode.next = self.current
        (self.current.prev).next = newNode
        self.current.prev = newNode

    #이전 노드 삭제후 다음 노드를 연결
    def delete(self):
        if self.current.prev == self.head:
            return
        oldNode = self.current.prev
        (oldNode.prev).next = self.current
        self.current.prev = oldNode.prev
        del oldNode

    def print_list(self):
        """리스트의 모든 값 출력"""
        values = []
        
        # TODO: head부터 시작
        current = self.head.next
        
        # TODO: 끝까지 순회하며 값 수집
        while current != self.tail:
            values.append(current.data)
            current = current.next

        print(''.join(values))

import sys
line = list(sys.stdin.readline().strip())

ll = LinkedList()
for i in line:
    ll.insert(i)

n = int(sys.stdin.readline().strip())
for i in range(n):
    temp = list(sys.stdin.readline().strip().split())
    match temp[0]:
        case 'L':
            ll.back()
        case 'D':
            ll.go()
        case 'B':
            ll.delete()
        case 'P':
            ll.insert(temp[1])

ll.print_list()