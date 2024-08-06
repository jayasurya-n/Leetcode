from typing import List,Optional
from collections import deque
import sys
class MyQueue:
    def __init__(self):
        self.arr = []
        self.front = 0
        self.rear = 0 

    def push(self, x):
        self.arr.append(x)
        self.rear+=1 


    def pop(self):
        if(self.front==self.rear):return -1
        temp = self.arr[self.front]
        self.front+=1
        return temp

# time complexity: O(1)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = list(map(int,input().strip().split()))
        print(Solution().MyStack())