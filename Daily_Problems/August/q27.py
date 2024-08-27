from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int):
        adj = [[] for _ in range(n)]
        for i in range(len(edges)):
            u,v = edges[i]
            p = succProb[i]
            adj[u].append((v,p))
            adj[v].append((u,p))

        prob = [0]*n
        prob[start_node] = 1
        pq = [(-1,start_node)]
        
        while pq:
            prob_u,u = heapq.heappop(pq)
            if(u==end_node):return -prob_u
            for v,p in adj[u]:
                if(-prob_u*p > prob[v]):
                    prob[v] = -prob_u*p
                    heapq.heappush(pq,(-prob[v],v))
        
        return 0
            
# time complexity: O(elogv)
# space complexity: O(v+e)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))