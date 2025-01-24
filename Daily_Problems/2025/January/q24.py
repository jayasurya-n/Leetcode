from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        def dfs(u):
            visited[u] = True
            pathVisited[u] = True
            
            for v in graph[u]:
                if(not visited[v]):
                    if(dfs(v)):return True
                elif(visited[v] and pathVisited[v]):return True
            
            pathVisited[u] = False
            return False
                
        visited = [False]*n
        pathVisited = [False]*n
        for u in range(n):
            if(not visited[u]):dfs(u)
        
        ans = [i for i in range(len(pathVisited)) if pathVisited[i]==False]
        return ans
            
# time complexity: O(v+e)
# space complexity: O(v)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))