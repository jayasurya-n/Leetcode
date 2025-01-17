from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def minSteps(self, n: int):
        if(n==1):return 0
        
        def solve(curr,copied,dp):
            if(curr==n):return 0
            elif(curr>n):return 1000
            
            print(curr,copied)
            if(dp[curr][copied]!=-1):return dp[curr][copied]
            
            ope1 = 2+solve(curr*2,curr,dp)
            ope2 = 1+solve(curr+copied,copied,dp)
            dp[curr][copied] = min(ope1,ope2)
            return dp[curr][copied]
            
        dp = [[-1]*(n//2+1) for _ in range(n+1)]
        ope = 1+solve(1,1,dp)
        return ope

    def minSteps(self, n: int):  
        if(n==1):return 0          
        dp = [[sys.maxsize]*(n+1) for _ in range(n+1)]
        dp[1][0] = 0
        
        for i in range(1,n+1):
            for j in range(0,n//2+1):
                if(i+i<=n):
                    dp[i+i][i] = min(dp[i+i][i],2+dp[i][j])
                if(i+j<=n):
                    dp[i+j][j] = min(dp[i+j][j],1+dp[i][j]) 
        
        return min(dp[-1])
    
    def minSteps(self, n: int):       
        dp = [sys.maxsize]*(n+1)
        dp[1] = 0

        for i in range(2,n+1):
            for j in range(1,i//2+1):
                if(i%j==0):
                    dp[i] = min(dp[i],dp[j]+ i//j)
        return dp[n]
    
    def minSteps(self, n: int):  
        d = 2
        ans = 0
        while n>1:
            while n%d==0:
                ans+=d
                n//=d
            d+=1
        print("Ans")
        return ans
    
# time complexity: O(n^2),O(n^2),O(n^2),O(n)
# space complexity: O(n^2),O(n^2),O(n),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        print(Solution().minSteps(n))