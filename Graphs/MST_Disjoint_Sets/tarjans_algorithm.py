from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]):
        adj = [[] for _ in range(n)]
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        disc = [-1]*n
        low_disc = [-1]*n
        visited = [False]*n
        self.time = 0
        bridges = []
        
        def dfs(u,parent):
            print(u)
            visited[u]=True
            disc[u] = low_disc[u] = self.time
            self.time+=1
            
            for v in adj[u]:
                if(not visited[v]):
                    dfs(v,u)
                    low_disc[u] = min(low_disc[u],low_disc[v])
                    if(low_disc[v]>disc[u]):bridges.append([u,v])
                elif(visited[v] and v!=parent):
                    low_disc[u] = min(low_disc[u],low_disc[v])
                    
        dfs(0,-1)
        return bridges
        
# time complexity: O(v+e)
# space complexity: O(v+e)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        connections = [list(map(int,input().strip().split())) for _ in range(n)]
        print(Solution().criticalConnections(n,connections))