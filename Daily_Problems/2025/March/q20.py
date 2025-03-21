from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        
        def dfs(u,root,visited,cost,components):
            visited[u] = True
            components[u] = root
            for v,w in adj[u]:
                cost[root]&=w
                if(visited[v]):continue
                dfs(v,root,visited,cost,components)
        
        visited = [False]*n
        cost = [-1]*n
        components = list(range(n))
        
        for u in range(n):
            if(not visited[u]):dfs(u,u,visited,cost,components)
        
        ans = []
        for u,v in query:
            if(components[u]!=components[v]):ans.append(-1)
            else:ans.append(cost[components[u]])
        return ans

# time complexity: O(v+e+q)
# space complexity: O(v)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))