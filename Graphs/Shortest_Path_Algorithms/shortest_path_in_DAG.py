from typing import List,Optional
from collections import deque
import sys,math
class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]):
        visited =  [False]*n
        adj =  [[] for _ in range(n)] 
        for i in range(len(edges)):
            adj[edges[i][0]].append((edges[i][1],edges[i][2]))
        
        def dfs(u):
            visited[u] = True
            for v,d in adj[u]:
                if(not visited[v]):dfs(v)
            stack.append(u)
        
        stack = []
        for u in range(n):
            if(not visited[u]):dfs(u)

        distance = [sys.maxsize]*n
        distance[0] = 0
        while(stack):
            top = stack.pop()
            for v,d in adj[top]:
                distance[v] = min(distance[v],distance[top]+d)
        
        for i in range(len(distance)):
            if(distance[i]>=sys.maxsize):distance[i]=-1
        return distance 
    
# time complexity: O(n+e)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,m = list(map(int,input().strip().split()))
        edges = [list(map(int,input().strip().split())) for _ in range(m)]
        print(Solution().shortestPath(n,m,edges))