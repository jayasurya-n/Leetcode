from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # mod = 10**9+7
        # ans = pow(5,(n+1)//2,mod)
        # ans*= pow(4,n//2,mod)
        # ans%=mod
        # return ans
        
        mod = 10**9+7
        def power(a,b,mod):
            ans = 1
            while b:
                if(b%2):
                    ans*=a
                    ans%=mod
                    b-=1
                a*=a
                a%=mod
                b>>=1
            return ans
        
        ans = power(5,(n+1)//2,mod)
        ans*= power(4,n//2,mod)
        ans%=mod
        return ans

# time complexity: O(logn),O(logn)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        print(Solution().countGoodNumbers(n))