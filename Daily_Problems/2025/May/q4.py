from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hash = defaultdict(int)
        for x,y in dominoes:
            x,y = sorted([x,y])
            hash[(x,y)]+=1
        
        return sum([(val*(val-1))>>1 for val in hash.values()])

        hash = defaultdict(int)
        ans = 0
        for x,y in dominoes:
            x,y = sorted([x,y])
            ans+=hash[(x,y)]
            hash[(x,y)]+=1
        return ans

# time complexity: O(n),O(n)
# space complexity: O(n),O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))