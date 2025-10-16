from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def solve(l):
            if(l<=0):return 0
            start = 1
            val = 1
            ans = 0
            while start<=l:
                ans+=val*(min(4*start-1,l)-start+1)
                val+=1
                start*=4
            return ans
        
        ans = 0
        for l,r in queries:
            ans+=(solve(r)-solve(l-1)+1)//2
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))