from typing import List,Optional
from collections import deque
import sys, math, heapq

class DisjointSet:
    
    def __init__(self,n):
        self.size = [1]*(n+1)
        self.parent = [0]*(n+1)
        for i in range(n+1):self.parent[i] = i
    
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
    def largestIsland(self, grid: List[List[int]]):
        m,n = len(grid),len(grid[0])
        ds = DisjointSet(m*n)
        
        dx = [1,-1,0,0]
        dy = [0,0,1,-1] 
               
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    for k in range(4):
                        x = i+dx[k]
                        y = j+dy[k]
                        if(x<m and x>=0 and 
                           y<n and y>=0 and grid[x][y]==1):
                            ds.unionbySize(i*n+j, x*n+y)
        
        ans = 0
        water = False
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==0):
                    water = True
                    st = set()
                    for k in range(4):
                        x = i+dx[k]
                        y = j+dy[k]
                        if(x<m and x>=0 and 
                           y<n and y>=0 and grid[x][y]==1):
                            st.add(ds.findUltimateParent(x*n+y))
                    
                    cur_size = 1
                    for p in st:
                        cur_size+=ds.size[p]
                    ans = max(ans,cur_size)
                 
        return ans if water else m*n  
                                
# time complexity: O(mn*(4*alpha))
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        m,n = list(map(int,input().strip().split()))
        grid = [list(map(int,input().strip().split())) for _ in range(m)]
        print(Solution().largestIsland(grid))