from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        pstart,pend = 0,-1 
        
        ans = 0
        for i in range(len(meetings)):
            start,end = meetings[i]
            if(start>pend):
                ans+=pend-pstart+1
                pstart,pend = start,end 
            else:pend = max(end,pend)

        ans+=pend-pstart+1
        return days-ans

# time complexity: O(nlogn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))