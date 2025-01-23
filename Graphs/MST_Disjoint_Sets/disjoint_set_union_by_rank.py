from typing import List,Optional
from collections import deque
import sys, math, heapq

class DisjointSet:
    def __init__(self,n):
        self.rank = [0]*(n+1)
        self.parent = list(range(n+1))

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
            
# time complexity: O(1) or (4alpha) on single query
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        obj = DisjointSet(7)
        obj.unionbyRank(1,2)
        obj.unionbyRank(2,3)
        obj.unionbyRank(4,5)
        obj.unionbyRank(6,7)
        obj.unionbyRank(5,6)
        
        if(obj.findUltimateParent(3)==obj.findUltimateParent(7)):print("Same")
        else:print("Not Same")

        obj.unionbyRank(3,7)
        
        if(obj.findUltimateParent(3)==obj.findUltimateParent(7)):print("Same")
        else:print("Not Same")        
        
        