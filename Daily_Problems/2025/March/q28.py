from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

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
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # m,n = len(grid),len(grid[0])
        # squeries = [(num,i) for i,num in enumerate(queries)]
        # squeries.sort()
        
        # q = [(grid[0][0],0,0)]
        # visited = [[False]*n for _ in range(m)]
        # visited[0][0] = True
        # ans = [0]*len(queries)
        # cnt = 0

        # for num,ind in squeries:
        #     while q and q[0][0]<num:
        #         _,x,y = heapq.heappop(q)
        #         cnt+=1
        #         for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
        #             nx,ny = x+dx,y+dy
        #             if(0<=nx<m and 0<=ny<n and not visited[nx][ny]):
        #                 heapq.heappush(q,(grid[nx][ny],nx,ny))
        #                 visited[nx][ny] = True
            
        #     ans[ind] = cnt
        # return ans
        
        # m,n,k = len(grid),len(grid[0]),len(queries)
        # effort = [10**9]*m*n #ni+j
        # pq = [(grid[0][0]+1,0,0)]
        # effort[0] = grid[0][0]+1
        
        # while pq:
        #     eff,x,y = heapq.heappop(pq)
        #     for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
        #         nx,ny = x+dx,y+dy
        #         if(0<=nx<m and 0<=ny<n and
        #            effort[nx*n+ny]>max(eff,1+grid[nx][ny])):
        #             effort[nx*n+ny] = max(eff,grid[nx][ny]+1)
        #             heapq.heappush(pq,(effort[nx*n+ny],nx,ny))
        
        # effort.sort()
        # def bsIndex(nums,target):
        #     # works like bisect.left
        #     # if target is lesser than smallest then index=0
        #     # if target is larger than largest  then index=n
        #     low,high = 0,len(nums)-1
        #     while(low<=high):
        #         mid = (low+high)>>1
        #         if(nums[mid]>target):high = mid-1
        #         else:low = mid+1
        #     return low
        
        # ans = []
        # for num in queries:ans.append(bsIndex(effort,num))
        # return ans

        m,n,k = len(grid),len(grid[0]),len(queries)
        sorted_queries = [(num,i) for i,num in enumerate(queries)]
        sorted_queries.sort()
        ans = [0]*k
        
        cells = [(grid[i][j],i,j) for i in range(m) for j in range(n)]
        cells.sort()
        ds = DisjointSet(m*n)
        
        ind = 0
        for curr_num,i in sorted_queries:
            while(ind<m*n and cells[ind][0]<curr_num):
                val,x,y = cells[ind]
                for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
                    nx,ny = x+dx,y+dy
                    if(0<=nx<m and 0<=ny<n and grid[nx][ny]<curr_num):
                        ds.unionbySize(n*x+y,n*nx+ny)
                ind+=1
            
            ans[i] = ds.size[ds.findUltimateParent(0)] if grid[0][0]<curr_num else 0
            
        return ans
    
# time complexity: O(mnlogmn+qlogq+q*alpha(mn))
# space complexity: O(mn+q)

# time complexity: O(mnlogmn+qlogq),O(mnlogmn+qlogmn),O(mnlogmn+qlogq+q*alpha(mn))
# space complexity: O(mn+q),O(mn),O(mn+q)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))