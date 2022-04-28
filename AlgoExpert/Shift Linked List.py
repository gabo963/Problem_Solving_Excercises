# -*- coding: utf-8 -*-
"""
AlgoExpert

Shift Linked List
"""

nodes = [
  {"id": "0", "next": "1", "value": 0},
    {"id": "1", "next": "2", "value": 1},
    {"id": "2", "next": "3", "value": 2},
    {"id": "3", "next": "4", "value": 3},
    {"id": "4", "next": "5", "value": 4},
    {"id": "5", "next": None, "value": 5} ]

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def Iniciar(nodes, step):
    
    lista = None
    
    if step == len(nodes)-1:
        lista = LinkedList( nodes[step]["value"] )
    else:
        lista = LinkedList( nodes[step]["value"] )
        lista.next = Iniciar(nodes, step + 1)
    
    return lista

def linkedListToArray(head):
    array = []
    current = head
    while current is not None:
        array.append(current.value)
        current = current.next
    return array

head = Iniciar(nodes, 0)
k = -2

def shiftLinkedList(head, k):
    # Write your code here.
    
    if len(linkedListToArray(head)) == 1 or k == 0:
        return head
    
    for i in range(abs(k)):
        store = None
        current = head
        
        if k > 0:
            while current.next.next != None:
                current = current.next
            
            store = current.next
            current.next = None
            store.next = head
            head = store
        else:
            store = head.next
            
            while current.next != None:
                current = current.next
            
            head.next = None
            current.next = head
            head = store
    
    return(head)

print("Head: " + str(linkedListToArray(head)))
print("k: " + str(k))
print("Solution: " + str(linkedListToArray(shiftLinkedList(head, k))))