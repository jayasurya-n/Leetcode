from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        adj = [[] for _ in range(n)]
        
        for i in range(n):
            if(edges[i]==-1):continue
            adj[i].append(edges[i])

        def bfs(adj,start):
            dis = [-1]*n
            dis[start] = 0
            q = deque([start])

            while q:
                u = q.popleft()
                for v in adj[u]:
                    if(dis[v]==-1):
                        dis[v] = dis[u]+1
                        q.append(v)
            return dis

        dis1 = bfs(adj,node1)
        dis2 = bfs(adj,node2)

        ans = 2*n
        ind = None
        for u in range(n):
            if(dis1[u]==-1 or dis2[u]==-1):continue
            maxi = max(dis1[u],dis2[u])
            if(ans>maxi):
                ans = maxi
                ind = u
        return ind if ans!=2*n else -1

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))