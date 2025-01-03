from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxheap = [-gift for gift in gifts]
        heapq.heapify(maxheap)
        
        for _ in range(k):
            top = -heapq.heappop(maxheap)
            heapq.heappush(maxheap,-math.floor(top**(0.5)))
        return -sum(maxheap)
            
# time complexity: O(n+klogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))