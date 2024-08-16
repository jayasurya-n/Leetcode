from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]):
        adj = [[] for _ in range(n)]
        for u,v,t in roads:
            adj[u].append((v,t))
            adj[v].append((u,t))
        
        mod = 10**9+7
        time = [sys.maxsize]*n
        time[0] = 0
        paths = [0]*n
        paths[0] = 1
        pq = [(0,0)]
        
        while(pq):
            t_u,u = heapq.heappop(pq)
            for v,t_v in adj[u]:
                if(t_v+t_u < time[v]):
                    time[v] = t_v+t_u
                    heapq.heappush(pq,((time[v],v)))
                    paths[v] = paths[u]
                elif(t_v+t_u == time[v]):
                    paths[v]= (paths[v]+paths[u])%mod
        return paths[n-1]%mod

# time complexity: O(elogv)
# space complexity: O(v)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))