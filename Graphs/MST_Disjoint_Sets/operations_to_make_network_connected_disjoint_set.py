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
    def makeConnected(self, n: int, connections: List[List[int]]):
        extra = 0
        ds = DisjointSet(n)
        
        for u,v in connections:
            if(ds.findUltimateParent(u)!=ds.findUltimateParent(v)):
                ds.unionbyRank(u,v)
            else:extra+=1
        
        components = 0
        for u in range(n):
            if(ds.parent[u]==u):components+=1
        
        if(extra<components-1):return -1
        else:return components-1


# time complexity: O((v+e)*(4*alpha))
# space complexity: O(v)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))