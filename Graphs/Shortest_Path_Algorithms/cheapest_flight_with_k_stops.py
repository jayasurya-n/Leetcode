from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = [[] for _ in range(n)]
        
        for i in range(len(flights)):
            u,v,w = flights[i]
            adj[u].append((v,w))
        
        distance = [sys.maxsize]*n
        distance[src] = 0
        q = deque([(0,src,0)])
        
        while q:
            stops,u,u_dist = q.popleft()
            if(stops>k):continue
            
            for v,w in adj[u]:
                if(w+u_dist<distance[v]):
                    distance[v] = w+u_dist
                    q.append((stops+1,v,distance[v]))
        
        return distance[dst] if distance[dst]!=sys.maxsize else -1            
        

# time complexity: O(k*e)
# space complexity: O(v+e)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))