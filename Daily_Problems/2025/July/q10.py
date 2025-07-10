from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        pmax = [-1]
        for i in range(n):
            curr = startTime[i]-(endTime[i-1] if i>0 else 0)
            pmax.append(max(pmax[-1],curr))
        
        smax = [-1]
        for i in range(n-1,-1,-1):
            curr = (startTime[i+1] if i+1<n else eventTime)-endTime[i]
            smax.append(max(smax[-1],curr))

        ans = 0
        for i in range(1,n+1):
            time = endTime[i-1]-startTime[i-1]
            g1 = startTime[i-1]-(endTime[i-2] if i>1 else 0)
            g2 = (startTime[i] if i<n else eventTime)-endTime[i-1]
            ans = max(ans,g1+g2)
            if(pmax[i-1]>=time or smax[n-i]>=time):
                ans = max(ans,g1+g2+time)
        return ans

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))