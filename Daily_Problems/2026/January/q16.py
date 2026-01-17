from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.sort()
        vFences.sort()

        hFences = [1]+hFences+[m]
        vFences = [1]+vFences+[n]

        hash = set()
        for i in range(1,len(hFences)):
            curr = 0
            for j in range(i,len(hFences)):
                curr+=hFences[j]-hFences[j-1]
                hash.add(curr)
        
        max_side = 0
        for i in range(1,len(vFences)):
            curr = 0
            for j in range(i,len(vFences)):
                curr+=vFences[j]-vFences[j-1]
                if(curr in hash):
                    max_side = max(max_side,curr)
        
        ans = max_side*max_side%(10**9+7)
        return ans if ans!=0 else -1

# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))