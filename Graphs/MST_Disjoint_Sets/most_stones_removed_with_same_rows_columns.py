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

class Solution:
    def removeStones(self, stones: List[List[int]]):
        r,c = 0,0
        for i,j in stones:
            r = max(r,i+1)
            c = max(c,j+1)
            
        ds = DisjointSet(r+c)
        for i,j in stones:
            ds.unionbySize(i,j+r)

        # counting parents of each stone 
        components = set(ds.findUltimateParent(i) for i,j in stones)
        return len(stones)-len(components)
        
        # from ds.size check
        # components = zero_stones = 0
        # for u in range(r+c+1):
        #     if(ds.findUltimateParent(u)==u):
        #         components+=1
        #         if(ds.size[u]==1):zero_stones+=1
        # return len(stones)-(components-zero_stones)
        
        # from parent(u)==u check
        # components = set()
        # for i,j in stones:
        #     if(ds.findUltimateParent(i)==i):components.add(i)
        #     elif(ds.findUltimateParent(j+r)==j+r):components.add(j+r)
        # print(components)
        # return len(stones)-len(components)

# time complexity: O((m+n)*(4*alpha))
# space complexity: O(m+n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))