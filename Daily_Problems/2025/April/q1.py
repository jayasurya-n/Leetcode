from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        
        # dp[i] = max points acheibale from question i till n
        # transition: dp[i] = max(dp[i+1],dp[i+question[i][1]+1])
        # final: dp[0]
        # base case: dp[n-1] = question[n-1][0]
        
        dp = [0]*n
        dp[n-1] = questions[n-1][0]
        
        for i in range(n-2,-1,-1):
            dp[i] = dp[i+1]
            val,shift = questions[i] 
            if(i+shift+1<n):dp[i] = max(dp[i],dp[i+shift+1]+val)
            else:dp[i] = max(dp[i],val)
        return dp[0]

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))