from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        m,n = len(robot),len(factory)
        robot.sort()
        factory.sort()
        dp = [[sys.maxsize]*(n+1) for _ in range(m+1)]
        for j in range(n+1):dp[0][j] = 0
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = dp[i][j-1]
                dist = 0
                for k in range(1,min(i,factory[j-1][1])+1):
                    dist+=abs(robot[i-k]-factory[j-1][0])
                    dp[i][j] = min(dp[i][j],dp[i-k][j-1]+dist)
        return dp[m][n]
                    
# time complexity: O(mn*capacity)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))