from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def evaluateExp(exp: str) -> int:
        n = len(exp)
        mod = 10**9+7
        dp = [[None]*n for _ in range(n)]
        for i in range(n):
            if(exp[i]=='T'):dp[i][i]=[1,0]
            elif(exp[i]=='F'):dp[i][i]=[0,1]
        
        for l in range(3,n+1,2):
            for i in range(0,n-l+1,2):
                j = i+l-1
                dp[i][j] = [0,0]
                for k in range(i+1,j,2):
                    t1,f1 = dp[i][k-1]
                    t2,f2 = dp[k+1][j]
                    if(exp[k]=='&'):
                        dp[i][j][0] = (dp[i][j][0]+t1*t2)%mod
                        dp[i][j][1] = (dp[i][j][1]+t1*f2+t2*f1+f1*f2)%mod
                    elif(exp[k]=='|'):
                        dp[i][j][0] = (dp[i][j][0]+t1*t2+t2*f1+t1*f2)%mod
                        dp[i][j][1] = (dp[i][j][1]+f1*f2)%mod
                    elif(exp[k]=='^'):
                        dp[i][j][0] = (dp[i][j][0]+t1*f2+t2*f1)%mod
                        dp[i][j][1] = (dp[i][j][1]+t1*t2+f1*f2)%mod
        return dp[0][n-1][0]
                    
# time complexity: O(n^3)
# space complexity: O(n^2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))