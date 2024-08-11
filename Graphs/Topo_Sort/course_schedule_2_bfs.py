from typing import List,Optional
from collections import deque
import sys
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]):
        n = numCourses
        e = len(prerequisites)
                    
        def bfs(start):
            q = deque(start)
            while q:
                u = q.popleft()
                ans.append(u)
                for v in adj[u]:
                    indegree[v]-=1
                    if(indegree[v]==0):q.append(v)
        
        adj = [[]*e for _ in range(n)]
        for i in range(e):adj[prerequisites[i][1]].append(prerequisites[i][0])  
                  
        indegree = [0]*n
        for i in range(e):indegree[prerequisites[i][0]]+=1    
                    
        start = []
        for u in range(n):
            if(indegree[u]==0):start.append(u)
        
        ans = []
        bfs(start)
        return ans if len(ans)==n else []
            
# time complexity: O(n+e)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,e = list(map(int,input().strip().split()))
        adj = [[] for _ in range(e)]
        for _ in range(e):
            u,v = list(map(int,input().strip().split()))
            adj[u].append(v)
        print(adj)
        print(Solution().isCyclic(n,adj))