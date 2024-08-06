from typing import List,Optional
from collections import deque
import sys
class StockSpanner:
    
    def __init__(self):
        self.stack = []
        self.day = 0
        

    def next(self, price: int):
        ans = -1
        self.day+=1
        while(self.stack and self.stack[-1][0]<=price):self.stack.pop()
        if(self.stack==[]):ans = self.day
        else:ans = self.day-self.stack[-1][1]
        self.stack.append((price,self.day))
        return ans


# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))