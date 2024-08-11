from typing import List,Optional
from collections import deque
import sys
class Solution:
    def isBipartite(self, graph: List[List[int]]):
        n = len(graph)
        def bfs(start):
            q = deque([start])
            visited[start] = 0
            
            while q:
                size = len(q)
                for _ in range(size):
                    u = q.popleft()
                    color = visited[u]
                    for v in graph[u]:
                        if(visited[v]==-1):
                            visited[v] = 1-color
                            q.append(v)
                        elif(visited[v]==color):return False
            return True
        
        visited = [-1]*n
        for i in range(n):
            if(visited[i]==-1):
                if(bfs(i)==False):
                    return False

        return True

# time complexity: O(n+2e)
# space complexity: O(2n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))