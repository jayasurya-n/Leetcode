from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class DisjointSet:
    def __init__(self,n):
        self.rank = [0]*(n+1)
        self.parent = list(range(n+1))

    def findUltimateParent(self,u):
        if(u==self.parent[u]):return u
        self.parent[u] = self.findUltimateParent(self.parent[u])
        return self.parent[u]

    def unionbyRank(self,u,v):
        rootu = self.findUltimateParent(u)
        rootv = self.findUltimateParent(v)
        if(rootu==rootv):return

        rank_u = self.rank[rootu]
        rank_v = self.rank[rootv]

        if(rank_u < rank_v):self.parent[rootu] = rootv
        elif(rank_u > rank_v):self.parent[rootv] = rootu
        else:
            self.parent[rootv] = rootu
            self.rank[rootu]+=1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # n = len(edges)
        # adj = [[] for _ in range(n)]
        # for u,v in edges:
        #     adj[u-1].append(v-1)
        #     adj[v-1].append(u-1)
        
        
        # self.start = -1
        # visited = [False]*n
        # parent = [-1]*n
        
        # def dfs(u,p,parent):
        #     visited[u] = True
        #     for v in adj[u]:
        #         if(not visited[v]):
        #             parent[v] = u
        #             dfs(v,u,parent)
        #         elif(v!=p and self.start==-1):
        #             self.start = v
        #             parent[v] = u
        
        # dfs(0,-1,parent)  
        # node = self.start
        # hash = set()
        # while True:
        #     hash.add(node)
        #     node = parent[node]
        #     if(node==self.start):break
        
        
        # for i in range(len(edges)-1,-1,-1):
        #     u,v = edges[i]
        #     if(u-1 in hash and v-1 in hash):return [u,v]
        
        n = len(edges)
        ds = DisjointSet(n-1)
        for u,v in edges:
            if(ds.findUltimateParent(u-1)==ds.findUltimateParent(v-1)):return [u,v]
            ds.unionbyRank(u-1,v-1)
            
# time complexity: O(n),O(n)
# space complexity: O(n),O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))