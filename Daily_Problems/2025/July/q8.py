from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort(key=lambda x:x[1])
        ends = [events[i][1] for i in range(n)]

        dp = [[0]*(k+1) for _ in range(n)]
        # dp[i][j]: maximum value till index i, attending maximum j events
        for j in range(1,k+1):dp[0][j] = events[0][2]
        
        for i in range(1,n):
            start,end,value = events[i]
            prev = bisect.bisect_left(ends,start)
            for j in range(1,k+1):
                dp[i][j] = max(dp[i-1][j],
                               (dp[prev-1][j-1] if prev!=0 else 0)+value)

        return max(dp[n-1])

# time complexity: O(nk+nlogn)
# space complexity: O(nk)
if __name__ == "__main__":
    for _ in range(ii()):
        n,k = lii()
        events = []
        for _ in range(n):events.append(lii())
        print(Solution().maxValue(events,k))