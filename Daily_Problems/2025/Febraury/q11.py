from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n = len(part) 
        for ch in s:
            stack.append(ch)
            if len(stack)>=len(part) and stack[-n:]==list(part):
                for _ in range(n):stack.pop() 
        return "".join(stack)

# time complexity: O(mn)
# space complexity: O(m)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))