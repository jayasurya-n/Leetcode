from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        adj = [[] for _ in range(n+1)]
        for i in range(m):
            u,v,w = edges[i]
            adj[u].append((v,w))
            adj[v].append((u,w))
        
        distance = [sys.maxsize]*(n+1)
        distance[1] = 0
    
        parent = [0]*(n+1)
        
        for i in range(n+1):
            parent[i] = i
        
        
        pq = [(0,1)]
        path = dict({1:None})
        
        while pq:
            d,u = heapq.heappop(pq)
            for v,w in adj[u]:
                if(distance[v]>d+w):
                    distance[v] = d+w
                    parent[v] = u
                    heapq.heappush(pq,(d+w,v)) 
        
        if(distance[n]==sys.maxsize):return [-1]
        
        ans = []
        node = n
        while(parent[node]!=node):
            ans.append(node)
            node = parent[node]
        
        ans.append(1)
        ans.append(distance[n])
        return ans[::-1]
        
            
# time complexity: O(mlogn+n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))