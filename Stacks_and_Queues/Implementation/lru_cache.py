from typing import List,Optional
from collections import deque
import sys
class Node:
    def __init__(self, key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        

def printList(head):
    print("Linked List:",end="")
    while head:
        print(head.val,end = " ")
        head = head.next
    print()   
             
class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.map = dict()
        self.capacity = capacity
        
    def add(self,node):
        temp = self.head.next
        node.next = temp
        self.head.next = node
        temp.prev = node
        node.prev = self.head 
    
    def delete(self,node):
        back = node.prev
        front = node.next
        back.next = front
        front.prev = back
        node.next,node.prev = None,None
        
        
    def get(self, key: int):
        node = self.map.get(key)
        if(node==None):return -1
        
        self.delete(node)
        self.add(node)
        return node.val
        
    def put(self, key: int, value: int):                     
        node = self.map.get(key)
        if(node):
            node.val = value
            self.delete(node)
            self.add(node)
            return
             
        if(len(self.map)==self.capacity):
            self.map.pop(self.tail.prev.key)
            self.delete(self.tail.prev)
        
        node = Node(key,value)
        self.add(node)
        self.map[key] = node
                            
        
# time complexity: O(1) in overall
# space complexity: O(1) in overall
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        obj = LRUCache(2)
        obj.put(1,1)
        obj.put(2,2)
        printList(obj.head)
        print("Get:",obj.get(1))
        obj.put(3,3)
        printList(obj.head)
        print("Get:",obj.get(2))
        obj.put(4,4)
        printList(obj.head)
        print("Get:",obj.get(1))
        print("Get:",obj.get(3))
        print("Get:",obj.get(4))
        
        
        
        