from typing import List,Optional
from collections import deque
import sys
class MyStack:  
    def __init__(self):
        self.arr=[]
    
    def push(self,data):
        self.arr.append(data)
        
    def pop(self):
        self.arr.pop()


# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = list(map(int,input().strip().split()))
        print(Solution().MyStack())