from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def dijkstra(self, n, adj, src):
        pq = [(0,src)]
        distance = [sys.maxsize]*n
        distance[src] = 0
        while pq:
            d,u = heapq.heappop(pq)
            for v,w in adj[u]:
                if(distance[v]>d+w):
                    distance[v] = d+w
                    heapq.heappush(pq,(d+w,v))
        return distance


# time complexity: O(elogv)
# space complexity: O(v)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))