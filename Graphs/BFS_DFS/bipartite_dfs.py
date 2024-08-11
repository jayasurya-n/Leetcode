from typing import List,Optional
from collections import deque
import sys
class Solution:
    def isBipartite(self, graph: List[List[int]]):
        n = len(graph)
        def dfs(u,color):
            visited[u] = color
            for v in graph[u]:
                if(visited[v]==-1):
                    if(dfs(v,1-color)==False):return False
                elif(visited[v]==color):return False
            return True
        
        visited = [-1]*n
        for u in range(n):
            if(visited[u]==-1):
                if(dfs(u,0)==False):
                    return False
        return True

# time complexity: O(n+2e)
# space complexity: O(n+n(stack space))
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))