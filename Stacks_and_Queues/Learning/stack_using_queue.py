from typing import List,Optional
from collections import deque
import sys
class MyStack:
    
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)
        

    def pop(self) -> int:
        while(len(self.q1)>1):
            self.q2.append(self.q1.popleft())
        
        top = self.q1.popleft()
        while(self.q2):
            self.q1.append(self.q2.popleft())
        return top

    def top(self) -> int:
        while(len(self.q1)>1):
            self.q2.append(self.q1.popleft())
        
        top = self.q1.popleft()
        self.q2.append(top)
        while(self.q2):
            self.q1.append(self.q2.popleft())
        return top
        

    def empty(self) -> bool:
        return len(self.q1)==0
        


# time complexity: O()
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))