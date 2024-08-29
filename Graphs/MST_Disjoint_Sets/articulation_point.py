from typing import List,Optional
from collections import deque
import sys, math, heapq
sys.setrecursionlimit(10**6)

class Solution:
    def articulationPoints(self, n, adj):        
        disc = [-1]*n
        low_disc = [-1]*n
        visited = [False]*n
        self.time = 0
        articPoints = [False]*n
        
        self.child = 0
        def dfs(u,parent):
            visited[u]=True
            disc[u] = low_disc[u] = self.time
            self.time+=1
            
            for v in adj[u]:
                if(not visited[v]):
                    if(parent==-1):self.child+=1
                    dfs(v,u)
                    low_disc[u] = min(low_disc[u],low_disc[v])
                    if(low_disc[v]>=disc[u] and parent!=-1):articPoints[u]=True
                elif(visited[v] and v!=parent):
                    low_disc[u] = min(low_disc[u],disc[v])
                    
        dfs(0,-1)
        if(self.child>1):articPoints[0]=True
        ans = []
        for i in range(n):
            if(articPoints[i]):ans.append(i)
        return ans if len(ans)!=0 else [-1]
        
# time complexity: O(v+e)
# space complexity: O(v)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,e = list(map(int,input().strip().split()))
        connections = [list(map(int,input().strip().split())) for _ in range(e)]
        adj = [[] for _ in range(n)]
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        print(Solution().articulationPoints(n,adj))