from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

def factorial(n,mod):
    fac = [1]*(n+1)
    for i in range(1,n+1):
        fac[i] = (fac[i-1]*i)%mod
    return fac

def inverse_factorial(n,fac,mod):
    inv  = [1]*(n+1)
    inv[n] = pow(fac[n],mod-2,mod)
    for i in range(n-1,-1,-1):
        inv[i] = (inv[i+1]*(i+1))%mod
    return inv

def nCr(n,r,fac,inv,mod):
    if(n<r or n<0 or r<0):return 0
    return fac[n]*inv[r] %mod *inv[n-r] %mod

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:    
        mod = 10**9+7
        maxL = min(n,15)
            
        # dp[val][l]: ways to form the sequnce of length l ending with val
        # transition: for mul in range(2*val,maxValue+1,val):dp[mul][l]+=dp[val][l-1]
        # base case:  for val in range(1,maxValue+1):dp[val][1] = 1
        
        dp = [[0]*(maxL+1) for _ in range(maxValue+1)]        
        for val in range(1,maxValue+1):dp[val][1] = 1

        for val in range(1,maxValue+1):
            for l in range(2,maxL+1):
                for mul in range(2*val,maxValue+1,val):
                    dp[mul][l]+=dp[val][l-1]
                    dp[mul][l]%=mod
        
        fac = factorial(n,mod)
        inv = inverse_factorial(n,fac,mod)
        
        ans = 0
        for val in range(1,maxValue+1):
            for l in range(1,maxL+1):
                k = dp[val][l]
                if(k==0):continue
                ans+=nCr(n-1,l-1,fac,inv,mod)*k
                ans%=mod
        return ans
    
# time complexity: O(mlogm*15)
# space complexity: O(m*15)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))