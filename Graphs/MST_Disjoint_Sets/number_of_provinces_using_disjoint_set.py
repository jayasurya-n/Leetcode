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
    def numProvinces(self, adj, n):
        ds = DisjointSet(n)
        for u in range(n):
            for v in range(n):
                if(adj[u][v]==1):
                    ds.unionbyRank(u,v)
        
        cnt = 0
        for u in range(n):
            if(ds.parent[u]==u):cnt+=1 
        return cnt

# time complexity: O(n^2*(4*alpha))
# space complexity: O(n)