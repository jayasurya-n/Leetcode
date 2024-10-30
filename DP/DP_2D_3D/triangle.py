from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        h = len(triangle)
        dp = []
        for level in range(h):dp.append([0]*len(triangle[level]))
        dp[0][0] = triangle[0][0]
        
        for level in range(1,h):
            for j in range(len(dp[level])):
                ans = sys.maxsize
                if(j!=len(dp[level])-1):ans = min(ans,triangle[level][j]+dp[level-1][j])
                if(j!=0):ans = min(ans,triangle[level][j]+dp[level-1][j-1])
                dp[level][j] = ans
        return min(dp[h-1])

# time complexity: O(size)
# space complexity: O(size)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        m = int(input().strip())
        triangle = [list(map(int,input().strip().split())) for _ in range(m)]
        print(Solution().minimumTotal(triangle))