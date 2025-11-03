from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        n = len(colors)

        i = 0
        while i<n:
            tsum = maxi = neededTime[i]
            while(i+1<n and colors[i]==colors[i+1]):
                maxi = max(maxi,neededTime[i+1])
                tsum+=neededTime[i+1] 
                i+=1
            ans+=tsum-maxi
            i+=1
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))