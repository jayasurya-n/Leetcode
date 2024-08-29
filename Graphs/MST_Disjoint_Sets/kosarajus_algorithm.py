from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:    
    def kosaraju(self, n, adj):
        order = []
        def dfs(u,adj):
            visited[u] = True
            for v in adj[u]:
                if(not visited[v]):dfs(v,adj)
            order.append(u) 
        
        visited = [False]*n
        for u in range(n):
            if(not visited[u]):dfs(u,adj)
        
        # reverse the edges
        radj = [[] for _ in range(n)]
        for u in range(n):
            for v in adj[u]:
                radj[v].append(u)
        
        ans = 0
        visited = [False]*n
        while(order):
            u = order.pop()
            if(not visited[u]):
                dfs(u,radj)
                ans+=1
        return ans
            
# time complexity: O(v+e)
# space complexity: O(v+e)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))