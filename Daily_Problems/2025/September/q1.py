from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = []
        for p,t in classes:
            heapq.heappush(pq,((p-t)/(t*(t+1)),p,t))
        
        for _ in range(extraStudents):
            _,p,t = heapq.heappop(pq)
            p+=1
            t+=1
            heapq.heappush(pq,(((p-t)/(t*(t+1)),p,t)))
        
        ans = 0
        while pq:
            _,p,t = heapq.heappop(pq)
            ans+=(p/t)

        return round(ans/len(classes), 6)

# time complexity: O(n+mlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))