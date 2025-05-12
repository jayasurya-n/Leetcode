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
        dis = [[float('inf')]*n for _ in range(m)]
        
        pq = [(0,0,0,0)]
        dis[0][0] = 0
        
        while pq:
            t,i,j,parity = heapq.heappop(pq)
            if(i==m-1 and j==n-1):return t
            
            for di,dj in [(0,1),(0,-1),(-1,0),(1,0)]:
                ni,nj = i+di,j+dj
                if not (0<=ni<m and 0<=nj<n):continue
                nt = max(t,moveTime[ni][nj])+(1 if parity==0 else 2)
                if(nt<dis[ni][nj]):
                    dis[ni][nj] = nt
                    heapq.heappush(pq,(nt,ni,nj,1-parity))
        return -1
        
# time complexity: O(mnlogmn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))