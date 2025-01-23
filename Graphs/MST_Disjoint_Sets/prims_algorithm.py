from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    # A spanning tree is a subgraph of a connected, undirected graph(n vertices) 
    # that includes all the vertices of the original graph with minimum edges needed to 
    # maintain a connected structure and it is a tree(no cycles and connected). 
    # It has n-1 edges and n vertices as it is a tree
    # A graph can have multiple spanning trees 
    
    def spanningTree(self, n, adj):
        pq = [(0,0)]
        visited = [False]*n
        sum = 0
        while pq:
            w,u = heapq.heappop(pq)
            if(visited[u] == True):continue
            visited[u] = True
            sum+=w
            
            for v,w in adj[u]:
                if(not visited[v]):
                    heapq.heappush(pq,(w,v))
        return sum

# time complexity: O(eloge)
# space complexity: O(v+e)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))