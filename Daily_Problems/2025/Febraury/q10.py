from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch.isdigit():stack.pop()
            else:stack.append(ch)
        return "".join(stack)

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))