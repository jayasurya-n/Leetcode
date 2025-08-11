from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10**9+7
        arr = []
        i = 0
        while n:
            if(n%2==1):arr.append(1<<i)
            n//=2
            i+=1
        
        pmul = [1]*(len(arr)+1)
        for i in range(1,len(arr)+1):
            pmul[i] = pmul[i-1]*arr[i-1]%mod
        
        ans = []
        for l,r in queries:
            res = pmul[r+1]
            res=res*pow(pmul[l],mod-2,mod)%mod
            ans.append(res)
        
        return ans

# time complexity: O(logn+q)
# space complexity: O(logn)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))