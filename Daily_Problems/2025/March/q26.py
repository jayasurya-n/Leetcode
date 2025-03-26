from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m,n = len(grid),len(grid[0])
        arr = []
        for i in range(m):
            for j in range(n):
                if(grid[i][j]%x!=grid[0][0]%x):return -1
                arr.append(grid[i][j])
        
        arr.sort()
        prefix = [arr[0]]
        for i in range(1,m*n):prefix.append(prefix[-1]+arr[i])
        
        tsum = sum(arr)
        ans = 10**18
        for i in range(m*n):
            curr = tsum-2*prefix[i]
            curr+=arr[i]*(2*i+2-m*n)
            curr//=x
            ans = min(ans,curr)
        return ans

# time complexity: O(mnlogmn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))