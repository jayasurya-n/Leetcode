from typing import List,Optional
from collections import deque
import sys

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class MyStack:
    
    def __init__(self):
        self.head = None
        
    def push(self, data):
        temp = StackNode(data)
        temp.next = self.head
        self.head = temp
            

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