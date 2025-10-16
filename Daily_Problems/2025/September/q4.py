from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1 = abs(x-z)
        d2 = abs(y-z)
        if(d1==d2):return 0
        return 1 if d1<d2 else 2

# time complexity: O(1)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))