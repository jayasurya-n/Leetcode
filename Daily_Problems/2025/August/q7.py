from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        collected = 0

        dp = [[-10**10]*n for _ in range(n)]
        dp[n-1][0] = fruits[n-1][0]

        for j in range(1,n):
            for i in range(j+1,n):
                top = dp[i-1][j-1] if i-1>=0 else 0
                level = dp[i][j-1]
                bottom = dp[i+1][j-1] if i+1<n else 0
                dp[i][j] = fruits[i][j]+max(top,level,bottom)

        # for row in dp:print(row)
        collected+=dp[n-1][n-2]

        dp = [[-10**10]*n for _ in range(n)]
        dp[0][n-1] = fruits[0][n-1]

        for i in range(1,n):
            for j in range(i+1,n):
                left = dp[i-1][j-1] if j-1>=0 else 0
                level = dp[i-1][j] 
                right = dp[i-1][j+1] if j+1<n else 0
                dp[i][j] = fruits[i][j]+max(left,level,right)
        
        # for row in dp:print(row)
        collected+=dp[n-2][n-1]

        for i in range(n):collected+=fruits[i][i]
        return collected
        

# time complexity: O(n^2+n)
# space complexity: O(n^2)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        fruits = []
        for _ in range(n):fruits.append(lii())
        print(Solution().maxCollectedFruits(fruits))