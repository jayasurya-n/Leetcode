from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = defaultdict(int)
        for b in basket1:freq[b]+=1
        for b in basket2:freq[b]-=1

        merge = []
        for b,f in freq.items():
            f = abs(f)
            if(f%2!=0):return -1
            merge.extend([b]*(f//2))
        
        if(not merge):return 0
        merge.sort()
        mini = min(min(basket1),min(basket2))
        return sum(min(2*mini,b) for b in merge[:len(merge)//2])
 
# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))