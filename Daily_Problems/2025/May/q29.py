from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n,m = len(edges1),len(edges2)
        n+=1;m+=1
        adj1 = [[] for _ in range(n)]
        adj2 = [[] for _ in range(m)]

        for u,v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)

        for u,v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)
        
        def bfs(root,adj):
            n = len(adj)
            visited = [False]*n
            visited[root] = True
            q = deque([(root,0)])
            nodes = [-1]*n
            nodes[root] = 0
            
            while q:
                u,d = q.popleft()
                nodes[u] = d%2
                for v in adj[u]:
                    if(visited[v]):continue
                    visited[v] = True
                    q.append((v,d+1))
            return nodes

        nodes1 = bfs(0,adj1)
        nodes2 = bfs(0,adj2)

        even1,odd1 = nodes1.count(0),nodes1.count(1)
        even2,odd2 = nodes2.count(0),nodes2.count(1)

        return [max(even2,odd2)+(even1 if nodes1[u]==0 else odd1)
                for u in range(n)]

# time complexity: O(n+m)
# space complexity: O(n+m)
if __name__ == "__main__":
    for _ in range(ii()):
        edges1 = lii()
        edges2 = lii()
        print(Solution().maxTargetNodes(edges1,edges2))