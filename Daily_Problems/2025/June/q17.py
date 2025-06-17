from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # total adjacent pairs:n-1, need to get n-1-k different adjacent pairs 
        # total n-k segments results in n-1-k boundaires 
        # this also make k matching pairs
        # formula: m*((m-1)^(n-k-1))*(n-1)C(n-k-1)

        mod = 10**9+7
        def fac(n):
            ans = 1
            for i in range(2,n+1):
                ans = (ans*i)%mod
            return ans

        ans = m
        ans= (ans*pow(m-1,n-k-1,mod))%mod
        ans= (ans*fac(n-1))%mod
        ans= (ans*pow(fac(k),mod-2,mod))%mod
        ans= (ans*pow(fac(n-k-1),mod-2,mod))%mod
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))