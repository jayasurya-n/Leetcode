from typing import List,Optional
from collections import deque
import sys
class Solution:
    def dfsOfGraph(self, n: int, adj: List[List[int]]):
        def dfs(u,ans):
            visited[u] = True
            ans.append(u)
            for v in adj[u]:
                if(not visited[v]):dfs(v,ans)
        
        visited = [False]*n
        ans = []
        dfs(0,ans)
        return ans
        

# time complexity: O(n+2e)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        adj = [list(map(int,input().strip().split())) for _ in range(n)]
        print(Solution().dfsOfGraph(n,adj))