from typing import List,Optional
from collections import deque
import sys
class Solution:
    def isCycle(self, n: int, adj: List[List[int]]):
        def bfs(start):
            q = deque([(start,-1)])
            visited[start] = True
            
            while(q):
                size = len(q)
                for _ in range(size):
                    u,prev = q.popleft()
                    for v in adj[u]:
                        if(visited[v] and v!=prev):return 1
                        if(not visited[v]):
                            q.append((v,u))
                            visited[v] = True
            return 0
            
        visited = [False]*n
        cycle = 0
        for u in range(n):
            if(not visited[u]):
                cycle|=bfs(u)
        return cycle  


# time complexity: O(n+2e)
# space complexity: O(2n)
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