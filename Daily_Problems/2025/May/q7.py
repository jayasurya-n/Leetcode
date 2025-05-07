from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m,n = len(moveTime),len(moveTime[0])
        visited = [[False]*n for _ in range(m)]
        
        pq = [(0,0,0)]
        visited[0][0] = True
        
        while pq:
            t,i,j = heapq.heappop(pq)
            if(i==m-1 and j==n-1):return t
            
            for di,dj in [(0,1),(0,-1),(-1,0),(1,0)]:
                ni,nj = i+di,j+dj
                if(0<=ni<m and 0<=nj<n and not visited[ni][nj]):
                    nt = max(t,moveTime[ni][nj])+1
                    heapq.heappush(pq,(nt,ni,nj))
                    visited[ni][nj] = True
        
# time complexity: O(mnlogmn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))