from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        max_sqaure = [[0]*n for _ in range(m)]

        ans = 0
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]==0):continue
                val1 = max_sqaure[i-1][j-1] if i-1>=0 and j-1>=0 else 0
                val2 = max_sqaure[i-1][j] if i-1>=0 else 0
                val3 = max_sqaure[i][j-1] if j-1>=0 else 0
                max_sqaure[i][j] = 1+min(val1,val2,val3)
                ans+=max_sqaure[i][j]
        return ans

# time complexity: O(mn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))