from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        mini,maxi = 0,0
        csum = 0
        for i in range(len(differences)):
            csum+=differences[i]
            maxi = max(maxi,csum)
            mini = min(mini,csum)
        
        top = upper-maxi
        bot = lower-mini
        return top-bot+1 if top>=bot else 0

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))