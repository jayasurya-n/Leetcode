from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        
        for i in range(len(times)):
            u,v,t = times[i]
            adj[u].append((v,t))
         
         
        pq = [(0,k)]
        time = [sys.maxsize]*(n+1)
        time[0] = 0
        time[k] = 0
        while pq:
            u_t,u = heapq.heappop(pq)    
            for v,t in adj[u]:
                if(time[v]>t+u_t):
                    time[v] = t+u_t
                    heapq.heappush(pq,(t+u_t,v))
        
        return max(time) if max(time)!=sys.maxsize else -1
        


# time complexity: O(elogv)
# space complexity: O(v)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))