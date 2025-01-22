from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m,n = len(isWater),len(isWater[0])
        q = deque([])
        heights = [[-1]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if(isWater[i][j]==1):
                    q.append((0,i,j))
                    heights[i][j] = 0
        
        while q:
            h,i,j = q.popleft()
            for di,dj in [(0,1),(0,-1),(-1,0),(1,0)]:
                ni,nj = i+di,j+dj
                if(0<=ni<m and 0<=nj<n and heights[ni][nj]==-1):
                    heights[ni][nj] = h+1
                    q.append((h+1,ni,nj))
        return heights

# time complexity: O(mn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))