from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int):
        adj = [[] for _ in range(n)]
        for u,v,w in edges:
            if(w!=-1):
                adj[u].append((v,w))
                adj[v].append((u,w))
    
        def dijktras(src,dst,adj):                    
            min_dis = [sys.maxsize]*n
            min_dis[src] = 0
            pq = [(0,src)]
            
            while pq:
                d_u,u = heapq.heappop(pq)
                for v,w in adj[u]:
                    if(w+d_u<min_dis[v]):
                        min_dis[v] = w+d_u
                        heapq.heappush(pq,((min_dis[v],v)))
            
            return min_dis[dst]
        
        cur_minDist = dijktras(source,destination,adj)
        if(cur_minDist<target):return []
        if(cur_minDist==target):
            for i in range(len(edges)):
                u,v,w = edges[i]
                if (w==-1):edges[i][2] = target+1
            return edges

        for i in range(len(edges)):
            u,v,w = edges[i]
            if(w==-1):
                edges[i][2] = 1
                adj[u].append((v,1))
                adj[v].append((u,1))
                cur_minDist = dijktras(source,destination,adj)
                
                if(cur_minDist<=target):
                    edges[i][2]+= target-cur_minDist
                    for j in range(i+1,len(edges)):
                        if(edges[j][2]==-1):edges[j][2] = target+1
                    return edges
        return []
        
# time complexity: O(e^2logv)
# space complexity: O(e+v)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))