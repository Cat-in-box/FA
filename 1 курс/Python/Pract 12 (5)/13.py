# -*- coding: utf-8 -*-
print ('№13', end = ' ')
class Node:
    def __init__(self, cargo=None, go_previous=None, go_next=None):
        self.cargo = cargo
        self.previous = go_previous
        self.next = go_next
    def __str__(self):
        return str(self.cargo)
    def read_f(self):
        while self:
            self.cargo = len(f.readline())
            print(self.cargo, end = ' ')
            self = self.next
node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node5 = Node()
node6 = Node()
node7 = Node()
node8 = Node()
node9 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node2.previous = node1
node3.previous = node2
node4.previous = node3
node5.previous = node4
node6.previous = node5
node7.previous = node6
node8.previous = node7
node9.previous = node8
f = open('Doc.txt', 'r')
node1.read_f()
f.close()
print('')