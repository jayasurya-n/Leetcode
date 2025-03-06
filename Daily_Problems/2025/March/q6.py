from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        y = x = 0
        csum = csum_sq = 0
        curr = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ele = grid[i][j]
                x+=ele
                y+=ele*ele
                csum+=curr
                csum_sq+=curr*curr
                curr+=1
        
        diff = x-csum
        add = (y-csum_sq)//diff
        return [(add+diff)//2, (add-diff)//2]

# time complexity: O(n^2)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))