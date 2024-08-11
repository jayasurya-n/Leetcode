from typing import List,Optional
from collections import deque
import sys
class Solution:
    def isCycle(self, n: int, adj: List[List[int]]):
        def dfs(u,prev):
            visited[u] = True
            
            for v in adj[u]:
                if(visited[v] and v!=prev):return 1
                if(not visited[v]):
                    if(dfs(v,u)):return 1

            return 0
                
        visited = [False]*n
        cycle = 0
        for u in range(n):
            if(not visited[u]):
                cycle|=dfs(u,-1)
        return cycle  


# time complexity: O(n+2e)
# space complexity: O(n+n(stack space))
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,e = list(map(int,input().strip().split()))
        adj = [[] for _ in range(e)]
        for _ in range(e):
            u,v = list(map(int,input().strip().split()))
            adj[u].append(v)
            adj[v].append(u)
        print(adj)
        print(Solution().isCycle(n,adj))