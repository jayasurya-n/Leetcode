from typing import List,Optional
from collections import deque
import sys, math, heapq

class DisjointSet:
    
    def __init__(self,n):
        self.rank = [0]*(n+1)
        self.parent = [0]*(n+1)
        for i in range(n+1):self.parent[i] = i
    
    def findUltimateParent(self,u):
        if(u==self.parent[u]):return u
        self.parent[u] = self.findUltimateParent(self.parent[u])
        return self.parent[u]

    def unionbyRank(self,u,v):
        ulp_u = self.findUltimateParent(u) 
        ulp_v = self.findUltimateParent(v)
        
        if(ulp_u==ulp_v):return 
        
        rank_u = self.rank[ulp_u] 
        rank_v = self.rank[ulp_v]
        
        if(rank_u < rank_v):self.parent[ulp_u] = ulp_v
        elif(rank_u > rank_v):self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u]+=1


class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]):
        matrix = [[0]*cols for _ in range(rows)]
        ds = DisjointSet(rows*cols)
        
        ans = []
        cnt = 0
        for i,j in operators:
            node = cols*i+j
            if(matrix[i][j] == 1):
                ans.append(cnt)
                continue
            matrix[i][j] = 1
            cnt+=1
            
            dx = [1,-1,0,0]
            dy = [0,0,1,-1]
            for k in range(4):
                x = i+dx[k]
                y = j+dy[k]
                if(x<rows and x>=0 and 
                   y<cols and y>=0 and matrix[x][y]==1):
                    adjNode = cols*x+y 
                    if(ds.findUltimateParent(node)!=ds.findUltimateParent(adjNode)):
                        ds.unionbyRank(node,adjNode)
                        cnt-=1 
            ans.append(cnt)
        return ans
    
# time complexity: O(mn*(4*alpha))
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        m = int(input().strip())
        k = int(input().strip())
        operators = [list(map(int,input().strip().split())) for _ in range(k)]
        print(Solution().numOfIslands(n,m,operators))