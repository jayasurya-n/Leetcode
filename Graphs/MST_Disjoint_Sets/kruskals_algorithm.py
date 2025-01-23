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
            
class Solution:
    # A spanning tree is a subgraph of a connected, undirected graph(n vertices) 
    # that includes all the vertices of the original graph with minimum edges needed to 
    # maintain a connected structure and it is a tree(no cycles and connected). 
    # It has n-1 edges and n vertices as it is a tree
    # A graph can have multiple spanning trees 
    
    def spanningTree(self, n, adj):
        edges = []
        for u in range(n):
            for v,w in adj[u]:
                if(v>u):edges.append((w,(u,v)))
        
        edges.sort()
        ds = DisjointSet(n)
        sum = 0
        for w,(u,v) in edges:
            if(ds.findUltimateParent(u)!=ds.findUltimateParent(v)):
                sum+=w
                ds.unionbyRank(u,v)
        return sum

# time complexity: O(v+e + eloge + e(4*alpha))
# space complexity: O(v+e)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        v,e = list(map(int,input().strip().split()))
        edges = [list(map(int,input().strip().split())) for _ in range(e)]
        adj = [[] for _ in range(v)]
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        print(Solution().spanningTree(v,adj))