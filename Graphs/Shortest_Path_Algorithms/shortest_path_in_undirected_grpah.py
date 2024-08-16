from typing import List,Optional
from collections import deque
import sys,math
class Solution:
    def shortestPath(self, edges, n, m, src):
        distance = [sys.maxsize]*n
        adj = [[] for _ in range(n)]
        
        for i in range(m):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])
            
        
        def bfs(src):
            q = deque([(src,0)])
            distance[src] = 0
            
            while q:
                size = len(q)
                for _ in range(size):
                    u,d = q.popleft()
                    for v in adj[u]:
                        if(distance[v]>d+1):
                            distance[v] = d+1
                            q.append((v,distance[v]))
                        
        bfs(src)
        for i in range(len(distance)):
            if(distance[i]>=sys.maxsize):distance[i]=-1
        return distance 
    
# time complexity: O(n+e)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,m,src = list(map(int,input().strip().split()))
        edges = [list(map(int,input().strip().split())) for _ in range(m)]
        print(Solution().shortestPath(edges,n,m,src))