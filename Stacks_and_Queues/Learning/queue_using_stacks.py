from typing import List,Optional
from collections import deque
import sys
class MyQueue:
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self):
        while(len(self.stack1)>1):
            self.stack2.append(self.stack1.pop())
        
        top = self.stack1.pop()
        while(self.stack2):
            self.stack1.append(self.stack2.pop())
        return top

    def peek(self) -> int:
        while(len(self.stack1)>1):
            self.stack2.append(self.stack1.pop())
        
        top = self.stack1.pop()
        self.stack2.append(top)
        while(self.stack2):
            self.stack1.append(self.stack2.pop())
        return top


    def empty(self) -> bool:
        return self.stack1==[]



# time complexity: O()
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))