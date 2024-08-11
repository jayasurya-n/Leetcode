from typing import List,Optional
from collections import deque
import sys,math
class Solution:
    def topoSort(self, n, adj):
        def bfs(start):
            q = deque(start)
            
            while q:
                u = q.popleft()
                ans.append(u)
                for v in adj[u]:
                    indegree[v]-=1
                    if(indegree[v]==0):q.append(v)
            
        indegree = [0]*n
        for u in range(n):
            for v in adj[u]:
                indegree[v]+=1
                
        start = []
        for u in range(n):
            if(indegree[u]==0):start.append(u)
        ans = []
        bfs(start)
        return ans
            
# time complexity: O(n+e)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,e = list(map(int,input().strip().split()))
        adj = [[] for _ in range(e)]
        for _ in range(e):
            u,v = list(map(int,input().strip().split()))
            adj[u].append(v)
        print(adj)
        print(Solution().isCyclic(n,adj))