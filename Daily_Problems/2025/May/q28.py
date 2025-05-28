from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
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
        
        def bfs(root,adj,k):
            n = len(adj)
            visited = [False]*n
            visited[root] = True
            q = deque([(root,0)])
            
            cnt = 0
            while q:
                u,d = q.popleft()
                if(d<=k):cnt+=1
                if(d==k):continue
                for v in adj[u]:
                    if(visited[v]):continue
                    visited[v] = True
                    q.append((v,d+1))
            
            return cnt

        max_target_2 = max([bfs(u,adj2,k-1) for u in range(m)])
        return [bfs(u,adj1,k)+max_target_2 for u in range(n)]

# time complexity: O(n^2+m^2+n+m)
# space complexity: O(n+m)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))