from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]):
        adj = [[] for _ in range(n)]
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False]*n
        def dfs(u):
            self.cnt+=1
            visited[u] = True
            for v in adj[u]:
                if(not visited[v]):dfs(v)
        
        extra = len(connections)
        components = 0
        for u in range(n):
            if(not visited[u]):
                self.cnt = 0
                components+=1
                dfs(u)
                extra-=self.cnt-1
        
        if(extra<components-1):return -1
        else:return components-1


# time complexity: O(v+e)
# space complexity: O(v(stack space))
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))