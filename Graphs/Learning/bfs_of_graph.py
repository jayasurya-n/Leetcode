from typing import List,Optional
from collections import deque
import sys
class Solution:
    def bfsOfGraph(self, n: int, adj: List[List[int]]):
        def bfs(start):
            q = deque([start])
            visited[start] = True
            ans = []
            while(q):
                size = len(q)
                for _ in range(size):
                    u = q.popleft()
                    ans.append(u)
                    
                    for v in adj[u]:
                        if(not visited[v]):
                            q.append(v)
                            visited[v] = True
            return ans
        
        visited = [False]*n
        return bfs(0)
        

# time complexity: O(n+2e)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        adj = [list(map(int,input().strip().split())) for _ in range(n)]
        # print(adj)
        print(Solution().bfsOfGraph(n,adj))