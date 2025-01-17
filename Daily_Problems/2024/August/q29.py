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
    def removeStones(self, stones: List[List[int]]):
        r,c = 0,0
        for i,j in stones:
            r = max(r,i)
            c = max(c,j) 
        r+=1
        c+=1
                  
        ds = DisjointSet(r+c)
        for i,j in stones:
            ds.unionbyRank(i,j+r)
        
        components = set(ds.findUltimateParent(i) for i,j in stones)
        return len(stones)-len(components)

# time complexity: O(n*(4*alpha))
# space complexity: O(n)