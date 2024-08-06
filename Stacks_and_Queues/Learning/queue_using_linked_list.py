from typing import List,Optional
from collections import deque
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class MyQueue:
    
    def __init__(self):
        self.head = None
        
    def push(self, data):
        if(self.head==None):self.head = Node(data)
        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = Node(data)
            
    def pop(self):
        if(self.head==None):return -1
        
        top = self.head.data
        temp = self.head.next
        self.head.next = None
        self.head = temp
        return top


# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = list(map(int,input().strip().split()))
        print(Solution().MyStack())