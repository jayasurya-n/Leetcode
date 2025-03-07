from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(n):
            primes = [True]*(n+1)
            primes[0] = primes[1] = False
            
            for i in range(2,int(n**0.5)+1):
                if(not primes[i]):continue
                for j in range(i*i,n+1,i):
                    if(primes[j]):primes[j] = False
            return primes
        
        primes = sieve(right)
        prev = None
        ans = 10**7
        l,r = -1,-1
        for i in range(left,right+1):
            if(primes[i]):
                if(not prev):prev = i
                else:
                    if(ans>i-prev):
                        ans = i-prev
                        l,r = prev,i
                    prev = i
        return [l,r]

# time complexity: O(nloglogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))