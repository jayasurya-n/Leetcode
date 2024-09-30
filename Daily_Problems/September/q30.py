from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class CustomStack:
    
    def __init__(self, maxSize: int):
        self.stack = []
        self.capacity = maxSize
        

    def push(self, x: int) -> None:
        if(len(self.stack)<self.capacity):
            self.stack.append(x)
        

    def pop(self) -> int:
        if(self.stack):return self.stack.pop()
        return -1
        

    def increment(self, k: int, val: int) -> None:
        for i in range(0,min(k,len(self.stack))):
            self.stack[i]+=val


# time complexity: O(1)
# space complexity: O(k)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))