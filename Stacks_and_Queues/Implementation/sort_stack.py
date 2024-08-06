from typing import List,Optional
from collections import deque
import sys
class Solution:
    def sortStack(self,stack):
        if(stack==[]):return 
        
        top = stack.pop()
        self.sortStack(stack)
        store = []
        while(stack and stack[-1]>top):store.append(stack.pop())
        stack.append(top)
        while(store):stack.append(store.pop())

# time complexity: O(n^2)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        Solution().sortStack(arr)
        print(arr)