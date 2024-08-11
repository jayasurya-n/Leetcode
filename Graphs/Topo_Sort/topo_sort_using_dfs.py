from typing import List,Optional
from collections import deque
import sys
class Solution:
    def topoSort(self, n, adj):
        def dfs(u):
            visited[u] = True
            
            for v in adj[u]:
                if(not visited[v]):dfs(v)
            ans.append(u)
            
        visited = [False]*n
        ans = []
        for u in range(n):
            if(not visited[u]):dfs(u)
        return ans[::-1]
            
# time complexity: O(n+2e)
# space complexity: O(n+n(stack space))
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,e = list(map(int,input().strip().split()))
        adj = [[] for _ in range(e)]
        for _ in range(e):
            u,v = list(map(int,input().strip().split()))
            adj[u].append(v)
        print(adj)
        print(Solution().isCyclic(n,adj))