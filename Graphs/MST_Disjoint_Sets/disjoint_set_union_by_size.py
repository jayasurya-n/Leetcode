from typing import List,Optional
from collections import deque
import sys, math, heapq

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

# time complexity: O(1) or (4alpha) on single query
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        obj = DisjointSet(7)
        obj.unionbySize(1,2)
        obj.unionbySize(2,3)
        obj.unionbySize(4,5)
        obj.unionbySize(6,7)
        obj.unionbySize(5,6)
        
        if(obj.findUltimateParent(3)==obj.findUltimateParent(7)):print("Same")
        else:print("Not Same")

        obj.unionbySize(3,7)
        
        if(obj.findUltimateParent(3)==obj.findUltimateParent(7)):print("Same")
        else:print("Not Same")        
        
        