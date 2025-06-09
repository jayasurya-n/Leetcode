from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k-=1
        def findBetween(curr1,curr2):
            ans = 0
            while curr1<=n:
                ans+=min(n+1,curr2)-curr1
                curr1*=10
                curr2*=10
            return ans

        while k>0:
            # numbers between [curr,curr+1) excluded
            between = findBetween(curr,curr+1)
            if(between<=k):
                k-=between
                curr+=1
            else:
                k-=1
                curr*=10
        return curr

# time complexity: O((logn)^2)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))