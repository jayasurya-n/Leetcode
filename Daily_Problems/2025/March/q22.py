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
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # adj = [[] for _ in range(n)]
        # degree = [0]*n
        # for u,v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        #     degree[u]+=1
        #     degree[v]+=1
        
        # def dfs(u,visited,vertices):
        #     visited[u] = True
        #     vertices.append(u)
        #     for v in adj[u]:
        #         if(visited[v]):continue
        #         dfs(v,visited,vertices)
        
        # ans = 0
        # visited = [False]*n
        # for i in range(n):
        #     if(not visited[i]):
        #         vertices = []
        #         dfs(i,visited,vertices)
        #         ok = True
        #         for v in vertices:
        #             if(degree[v]+1!=len(vertices)):
        #                 ok = False
        #                 break
        #         if(ok):ans+=1
        # return ans
        
        degree = [0]*n
        ds = DisjointSet(n)
        for u,v in edges:
            degree[u]+=1
            degree[v]+=1
            ds.unionbySize(u,v)
        
        roots = [True]*n
        for u in range(n):
            root = ds.findUltimateParent(u)
            if(u!=root):roots[u] = False
            size = ds.size[root]
            if(degree[u]!=size-1):roots[root] = False
        
        return sum([1 for u in range(n) if roots[u]])

# time complexity: O(n+e),O(n+e)
# space complexity: O(n+e),O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))