from typing import List,Optional
from collections import deque
import sys
class Solution:
    def isCyclic(self, n : int , adj : List[List[int]]):
        def dfs(u):
            visited[u] = True
            pathVisited[u] = True
            
            for v in adj[u]:
                if(not visited[v]):
                    if(dfs(v)):return 1
                elif(visited[v] and pathVisited[v]):return 1
                
            pathVisited[u] = False
            return 0
                
        visited = [False]*n
        pathVisited = [False]*n
        for u in range(n):
            if(not visited[u]):
                if(dfs(u)):return 1
        return 0

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