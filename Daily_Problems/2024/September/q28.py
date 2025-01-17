from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Node():
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None 
            
class MyCircularDeque:

    def __init__(self, k: int):
        self.dummy_head = Node(-1)
        self.dummy_rear = Node(-1)
        self.dummy_head.next = self.dummy_rear
        self.dummy_rear.prev = self.dummy_head
        self.capacity = k
        self.size = 0
        
        
    def insertFront(self, value: int) -> bool:
        if(self.size==self.capacity):return False
        node = Node(value)
        self.size+=1
        front = self.dummy_head.next
        self.dummy_head.next = node
        front.prev = node
        node.prev = self.dummy_head
        node.next = front
        return True
        

    def insertLast(self, value: int) -> bool:
        if(self.size==self.capacity):return False
        node = Node(value)
        self.size+=1
        back = self.dummy_rear.prev
        back.next = node
        self.dummy_rear.prev = node
        node.prev = back
        node.next = self.dummy_rear
        return True
        
    def deleteFront(self) -> bool:
        if(self.size==0):return False
        node = self.dummy_head.next
        self.size-=1
        front = node.next
        self.dummy_head.next = front
        front.prev = self.dummy_head
        node.next = None
        node.prev = None
        return True

    def deleteLast(self) -> bool:
        if(self.size==0):return False
        node = self.dummy_rear.prev
        self.size-=1
        back = node.prev
        self.dummy_rear.prev = back
        back.next = self.dummy_rear
        node.prev = None
        node.next = None
        return True
        
    def getFront(self) -> int:
        if(self.size==0):return -1
        return self.dummy_head.next.val

    def getRear(self) -> int:
        if(self.size==0):return -1
        return self.dummy_rear.prev.val
        
    def isEmpty(self) -> bool:
        return self.size==0
        
    def isFull(self) -> bool:
        return self.size==self.capacity
        

# time complexity: O(1)
# space complexity: O(k)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))