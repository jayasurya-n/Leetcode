from typing import List,Optional
from collections import deque
import sys

class Node:
    def __init__(self, key,val,cnt=1):
        self.key = key
        self.val = val
        self.cnt = cnt
        self.next = None
        self.prev = None

def printList(head):
    print("Linked List:",end="")
    while head:
        print(head.val,end = " ")
        head = head.next
    print()  

class DLL:
    def __init__(self):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def add(self,node):
        temp = self.head.next
        node.next = temp
        self.head.next = node
        temp.prev = node
        node.prev = self.head 
        self.size+=1
    
    def delete(self,node):
        back = node.prev
        front = node.next
        back.next = front
        front.prev = back
        node.next,node.prev = None,None 
        self.size-=1
             
             
class LFUCache:
    def __init__(self, capacity: int):
        self.freq = dict()
        self.map = dict()
        self.capacity = capacity
        self.minFreq = 0
        
        
    def get(self, key: int):
        node = self.map.get(key)
        if(node==None):return -1
        
        self.freq[node.cnt].delete(node)
        if(node.cnt==self.minFreq and self.freq[node.cnt].size==0):self.minFreq+=1
        node.cnt+=1 
        
        if(node.cnt in self.freq):self.freq[node.cnt].add(node)
        else:
            dll = DLL()
            self.freq[node.cnt] = dll
            dll.add(node)
        return node.val
        
    def put(self, key: int, value: int):                     
        node = self.map.get(key)
        if(node):
            node.val = value
            self.freq[node.cnt].delete(node)
            if(node.cnt==self.minFreq and self.freq[node.cnt].size==0):self.minFreq+=1
            node.cnt+=1 
            
            if(node.cnt in self.freq):self.freq[node.cnt].add(node)
            else:
                dll = DLL()
                self.freq[node.cnt] = dll
                dll.add(node)
            return
            
        if(len(self.map)==self.capacity):
            dll = self.freq[self.minFreq]
            self.map.pop(dll.tail.prev.key)
            dll.delete(dll.tail.prev)
        
        
        node = Node(key,value)
        self.minFreq = 1
        if(node.cnt not in self.freq):self.freq[node.cnt] = DLL()
        self.freq[node.cnt].add(node)
        self.map[key] = node            
        
# time complexity: O(1) in overall
# space complexity: O(1) in overall
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        obj = LFUCache(2)
        obj.put(1,1)
        obj.put(2,2)
        print("Get:",obj.get(1))
        obj.put(3,3)
        print("Get:",obj.get(2))
        print("Get:",obj.get(3))
        obj.put(4,4)
        print("Get:",obj.get(1))
        print("Get:",obj.get(3))
        print("Get:",obj.get(4))
        
        # obj = LFUCache(2)
        # obj.put(3,1)
        # obj.put(2,1)
        # obj.put(2,2)
        # obj.put(4,4)
        # print("Get:",obj.get(2))        