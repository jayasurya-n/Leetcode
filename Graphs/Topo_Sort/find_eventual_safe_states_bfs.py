from typing import List,Optional
from collections import deque
import sys
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]):
        n = len(graph)
        def bfs(start):
            q = deque(start)
            while q:
                u = q.popleft()
                ans.append(u)
                for v in graphReverse[u]:
                    indegree[v]-=1
                    if(indegree[v]==0):q.append(v)
                
        
        indegree = [0]*n
        graphReverse = [[] for _ in range(n)]
        
        for u in range(n):
            for v in graph[u]:
                indegree[u]+=1
                graphReverse[v].append(u)
        
        start = []
        for u in range(n):
            if(indegree[u]==0):start.append(u)
            
        ans = []
        bfs(start)
        ans.sort()
        return ans
            
# time complexity: O(n+e+nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,e = list(map(int,input().strip().split()))
        adj = [[] for _ in range(n)]
        for _ in range(e):
            u,v = list(map(int,input().strip().split()))
            adj[u].append(v)
        print(adj)
        print(Solution().isCyclic(n,adj))