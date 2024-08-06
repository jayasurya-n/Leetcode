from typing import List,Optional
from collections import deque
import sys
# class MinStack:
    
#     def __init__(self):
#         self.stack = []

#     def push(self, val: int):
#         if(self.stack==[]):self.stack.append((val,val))
#         else:
#             mini = self.stack[-1][1]
#             self.stack.append((val,min(mini,val)))
            

#     def pop(self):
#         self.stack.pop()
        

#     def top(self):
#         return self.stack[-1][0]
        

#     def getMin(self):
#         return self.stack[-1][1]

class MinStack:
    
    def __init__(self):
        self.stack = []
        self.min = sys.maxsize

    def push(self, val: int):
        if(self.stack==[]):
            self.stack.append(val)
            self.min = val
            return
        
        if(self.min<=val):
            self.stack.append(val)
        else:
            self.stack.append(2*val-self.min)
            self.min = val
            
            
    def pop(self):
        top  = self.stack[-1]
        if(top<self.min):
            self.min = 2*self.min-top
        self.stack.pop()

    def top(self):
        top  = self.stack[-1]
        if(top<self.min):
            return self.min
        return top
        
    def getMin(self):
        return self.min


# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))