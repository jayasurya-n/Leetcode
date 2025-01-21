from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        tsum1=sum(grid[0])
        sum1,sum2 = 0,0
        
        ans = sys.maxsize
        for j in range(n):
            sum1+=grid[0][j]
            ans = min(ans,max(tsum1-sum1,sum2))
            sum2+=grid[1][j]
        return ans
        
# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))