from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        
        visited = [-1]*n
        def isbipartite(u,val,adj):
            visited[u] = val
            for v in adj[u]:
                if(visited[v]==-1):
                    if(isbipartite(v,1-val,adj)==False):return False
                elif(visited[v]==val):return False
            return True

        for u in range(n):
            if(visited[u]==-1):
                if(isbipartite(u,0,adj)==False):return -1
        
        def find_maxdepth(start):
            q = deque([start])
            visited = [False]*n
            visited[start] = True
            d = 0
            
            while q:
                for _ in range(len(q)):
                    u = q.popleft()
                    for v in adj[u]:
                        if(not visited[v]):
                            visited[v] = True
                            q.append(v)
                d+=1
            return d
        
        depths = [-1]*n
        for u in range(n):
            depths[u] =  find_maxdepth(u)
        

        def find_groupsize(u):
            visited[u] = True
            groups = depths[u]
            
            for v in adj[u]:
                if(not visited[v]):groups = max(groups,find_groupsize(v))
            return groups
            
        visited = [False]*n
        ans = 0
        for u in range(n):
            if(not visited[u]):ans+=find_groupsize(u)
        return ans

# time complexity: O(v(v+e))
# space complexity: O(v)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))