from typing import List,Optional
from collections import deque
import sys
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]):
        n = numCourses
        e = len(prerequisites)
        adj = [[]*e for _ in range(n)]
        for i in range(e):adj[prerequisites[i][1]].append(prerequisites[i][0])
            
        def dfs(u):
            visited[u] = True
            pathVisited[u] = True
            
            for v in adj[u]:
                if(not visited[v]):
                    if(dfs(v)==False):return False
                elif(visited[v] and pathVisited[v]):return False
            
            ans.append(u)
            pathVisited[u] = False
            return True
            
        visited = [False]*n
        pathVisited = [False]*n
        ans = []
        for u in range(n):
            if(not visited[u]):
                if(dfs(u)==False):return []
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