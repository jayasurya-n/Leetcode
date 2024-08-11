from typing import List,Optional
from collections import deque
import sys
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]):
        n = len(graph)
        def dfs(u):
            visited[u] = True
            pathVisited[u] = True
            
            for v in graph[u]:
                if(not visited[v]):
                    if(dfs(v)):return True
                elif(visited[v] and pathVisited[v]):return True
            
            pathVisited[u] = False
            return False
                
        visited = [False]*n
        pathVisited = [False]*n
        for u in range(n):
            if(not visited[u]):dfs(u)
        
        ans = [i for i in range(len(pathVisited)) if pathVisited[i]==False]
        return ans
            
# time complexity: O(n+2e)
# space complexity: O(2n+n(stack space))
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,e = list(map(int,input().strip().split()))
        adj = [[] for _ in range(e)]
        for _ in range(e):
            u,v = list(map(int,input().strip().split()))
            adj[u].append(v)
        print(adj)
        print(Solution().isCyclic(n,adj))