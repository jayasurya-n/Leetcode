from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # dp = [0]*(k+maxPts)
        # dp[0] = 1
        
        # mul = (1/maxPts)
        # for i in range(1,k+maxPts): 
        #     for val in range(1,maxPts+1):
        #         if(i-val>=0 and i-val<k):
        #             dp[i]+=dp[i-val]*mul
        
        # ans = 0
        # for i in range(k,n+1):
        #     ans+=dp[i]
        # return round(ans,5)


        dp = [0]*(k+maxPts)
        dp[0] = 1
        
        s = 0
        for i in range(1,k+maxPts):
            if(i-1<k):s+=dp[i-1]
            if(i-maxPts>0):s-=dp[i-maxPts-1]
            dp[i] = s/maxPts
        
        ans = 0
        for i in range(k,min(n+1,k+maxPts)):
            ans+=dp[i]
        return round(ans,5)

# time complexity: O(k*maxi+n),O(k+maxi+n)
# space complexity: O(k*maxi),O(k+maxi+n)
if __name__ == "__main__":
    for _ in range(ii()):
        n,k,maxPts = lii()
        print(Solution().new21Game(n,k,maxPts))