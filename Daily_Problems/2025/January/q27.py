from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # visited = [False]*numCourses
        # path_visited = [False]*numCourses
        # reachble = defaultdict(set)
        
        # def dfs(u):
        #     visited[u] = True
        #     path_visited[u] = True
        #     hash = set()
        #     for v in adj[u]:
        #         hash.add(v)
        #         if(not visited[v]):hash|=dfs(v)
        #         elif(not path_visited[v] and visited[v]):hash|=reachble[v]
                    
        #     path_visited[u] = False
        #     reachble[u]=hash
        #     return hash
        
        # adj = [[] for _ in range(numCourses)]
        # for u,v in prerequisites:
        #     adj[u].append(v)
        
        # for u in range(numCourses):
        #     if(not dfs(u)):dfs(u)
        
        # ans = []
        # for u,v in queries:
        #     if(v in reachble[u]):ans.append(True)
        #     else:ans.append(False)
        # return ans
        
        
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for u,v in prerequisites:
            adj[u].append(v)
            indegree[v]+=1
        
        q = deque([])
        for u in range(numCourses):
            if(indegree[u]==0):q.append(u)
        
        node_prerequisites = defaultdict(set)
        
        while q:
            u = q.popleft()
            for v in adj[u]:
                node_prerequisites[v].add(u)
                node_prerequisites[v]|=node_prerequisites[u]
                indegree[v]-=1
                if(indegree[v]==0):q.append(v)
        
        ans = []
        for u,v in queries:
            if(u in node_prerequisites[v]):ans.append(True)
            else:ans.append(False)
        return ans
        
# time complexity: O((v+e)*e+q)
# space complexity: O(v^2+v)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))