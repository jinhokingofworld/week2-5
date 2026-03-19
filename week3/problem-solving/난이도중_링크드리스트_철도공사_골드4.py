# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309

#BP: i+1의 번호 출력, i와 i+1 사이에 j 삽입
#BN: i-1의 번호 출력, i와 i-1 사이에 j 삽입
#CN: i+1 노드 삭제, i+1 출력
#CP: i-1 노드 삭제, i-1 출력

class Node:
    def __init__(self, data: int):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.current = self.head

    #current Pointer의 앞에 삽입
    def append(self, number: int):
        newOne = Node(number)
        newOne.next = self.current.next
        newOne.prev = self.current
        (self.current.next).prev = newOne
        self.current.next = newOne
    
    #current Pointer의 앞을 삭제
    def deleteNext(self):
        oldOne = self.current.next
        (oldOne.next).prev = self.current
        self.current.next = (oldOne.next)
        sys.stdout.write(str(oldOne.data) + '\n')
        del oldOne

    #current Pointer의 뒤를 삭제
    def deleteBack(self):
        oldOne = self.current.prev
        (oldOne.prev).next = self.current
        self.current.prev = oldOne.prev
        sys.stdout.write(str(oldOne.data) + '\n')
        del oldOne

    def goTo(self, station):
        while self.current.data != station:
            self.go()
 
    def go(self):
        self.current = self.current.next

    def goBack(self):
        self.current = self.current.prev

    def printNext(self):
       sys.stdout.write(str(self.current.next.data) + '\n')
    
    def printBack(self):
       sys.stdout.write(str(self.current.prev.data) + '\n')

    def first_append(self, number):
        newOne = Node(number)
        if self.head == None:
            self.head = newOne
            self.current = newOne
            return
    
        while self.current.next != None:
            self.go()
        self.current.next = newOne
        newOne.prev = self.current

import sys

#역의 개수, 공사 개수
_, nums = map(int, sys.stdin.readline().strip().split())
#역번호 리스트
stations = list(map(int, sys.stdin.readline().strip().split()))
ll = LinkedList()

#기본역 채우기
for i in stations:
    ll.first_append(i)

#역 처음과 끝 연결하기
while ll.current.next != None:
    ll.current = ll.current.next
ll.current.next = ll.head
ll.head.prev = ll.current

#공사 시작
for i in range(nums):
    command = list(map(str, input().split()))
    command[1] = int(command[1])
    match command[0]:
        case 'BN':
            ll.goTo(command[1])
            ll.printNext()
            ll.append(int(command[2]))
        case 'BP':
            ll.goTo(command[1])
            ll.printBack()
            ll.goBack()
            ll.append(int(command[2]))
        case 'CP':
            ll.goTo(command[1])
            ll.deleteBack()
        case 'CN':
            ll.goTo(command[1])
            ll.deleteNext()