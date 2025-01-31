from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class DisjointSet:
    def __init__(self,n):
        self.size = [1]*(n+1)
        self.parent = list(range(n+1))

    def findUltimateParent(self,u):
        if(u==self.parent[u]):return u
        self.parent[u] = self.findUltimateParent(self.parent[u])
        return self.parent[u]

    def unionbySize(self,u,v):
        rootu = self.findUltimateParent(u)
        rootv = self.findUltimateParent(v)
        if(rootu==rootv):return

        size_u = self.size[rootu]
        size_v = self.size[rootv]

        if(size_u < size_v):
            self.parent[rootu] = rootv
            self.size[rootv]+=size_u
        else:
            self.parent[rootv] = rootu
            self.size[rootu]+=size_v

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        ds = DisjointSet(m*n)
        
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==0):continue
                for di,dj in [(0,1),(0,-1),(-1,0),(1,0)]:
                    ni,nj = i+di,j+dj
                    if(0<=ni<m and 0<=nj<n and grid[ni][nj]==1):
                        u,v = n*i+j,n*ni+nj
                        ds.unionbySize(u,v)
        
        root_parents = set()
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):root_parents.add(ds.findUltimateParent(n*i+j))
        
        ans = 0
        for rp in root_parents:ans=max(ans,ds.size[rp])
            
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):continue
                root_parents = set()
                for di,dj in [(0,1),(0,-1),(-1,0),(1,0)]:
                    ni,nj = i+di,j+dj
                    if(0<=ni<m and 0<=nj<n and grid[ni][nj]==1):
                        v = n*ni+nj
                        root_parents.add(ds.findUltimateParent(v))
                size = 1
                for rp in root_parents:size+=ds.size[rp]
                ans = max(ans,size)
        
        return ans
                        
# time complexity: O(mn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))