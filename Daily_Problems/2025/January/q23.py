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
        ulp_u = self.findUltimateParent(u)
        ulp_v = self.findUltimateParent(v)
        if(ulp_u==ulp_v):return

        size_u = self.size[ulp_u]
        size_v = self.size[ulp_v]

        if(size_u <= size_v):
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v]+=size_u
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u]+=size_v

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # m,n = len(grid),len(grid[0])
        # rows = [0]*m
        # cols = [0]*n
        
        # for i in range(m):
        #     for j in range(n):
        #         if(grid[i][j]==1):
        #             rows[i]+=1
        #             cols[j]+=1
        
        # isolated = 0
        # for i in range(m):
        #     for j in range(n):
        #         if(grid[i][j]==1 and rows[i]==1 and cols[j]==1):isolated+=1
        
        # return (sum(rows)+sum(cols))//2-isolated                    

        m,n = len(grid),len(grid[0])
        ds = DisjointSet(m+n)
        counts = [0]*(m+n)

        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):ds.unionbySize(i,j+m)
        
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    ultimate_parent = ds.findUltimateParent(i)
                    counts[ultimate_parent]+=1 
        return sum(cnt for cnt in counts if cnt>1)

# time complexity: O(mn),O(mn*(4alpha))
# space complexity: O(m+n),O(m+n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))