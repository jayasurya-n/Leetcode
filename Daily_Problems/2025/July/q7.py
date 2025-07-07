from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        last = max(event[1] for event in events)
        events.sort()

        ans = 0
        i = 0
        pq = []
        for day in range(1,last+1):
            while i<n and day==events[i][0]:
                heapq.heappush(pq,(events[i][1],events[i][0]))
                i+=1
            
            while(pq and day>pq[0][0]):heapq.heappop(pq)
            
            if(pq):
                ans+=1
                heapq.heappop(pq)
        
        return ans

# time complexity: O((n+d)logn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))