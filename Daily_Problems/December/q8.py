from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)        
        events.sort(key=lambda x:x[1])
        ends = [event[1] for event in events]
        
        dp = [0]*n
        dp[0] = events[0][2]
        for i in range(1,n):
            dp[i] = max(dp[i-1], events[i][2])
        
        ans = 0
        for i,(s,e,value) in enumerate(events):
            ind = bisect.bisect_right(ends,s-1)-1
            ans = max(ans,value+(dp[ind] if ind!=-1 else 0)) 
        return ans
            
# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))