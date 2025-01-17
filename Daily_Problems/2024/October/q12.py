from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for s,e in intervals:
            events.append((s,1))
            events.append((e+1,-1))
        
        events.sort()
        ans,cnt = 0,0
        for _,val in events:
            cnt+=val
            ans = max(ans,cnt)
        return ans
    
# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))