from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def maxPoints(self, points: List[List[int]]):
        m,n = len(points), len(points[0])
        
        dp = points[0]
        
        for i in range(1,m):
            left  = [0]*n
            left[0] = dp[0]
            for j in range(1,n):
                left[j] = max(dp[j],left[j-1]-1)
            
            right = [0]*n
            right[-1] = dp[-1]
            for j in range(n-2,-1,-1):
                right[j] = max(dp[j],right[j+1]-1)
            
            for j in range(n):
                dp[j] = points[i][j]+max(left[j],right[j]) 
            
        return max(dp)
             
# time complexity: O(n^2)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        m = int(input().strip())
        points = [list(map(int,input().strip().split())) for _ in range(m)]
        print(Solution().maxPoints(points))