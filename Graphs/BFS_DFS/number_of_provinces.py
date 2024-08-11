from typing import List,Optional
from collections import deque
import sys
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]):
        n = len(isConnected)
        def dfs(u):
            visited[u] = True
            for v in range(n):
                if(isConnected[u][v]==1 and not visited[v]):dfs(v)
        
        visited = [False]*n
        ans = 0
        for u in range(n):
            if(not visited[u]):
                ans+=1
                dfs(u)
        return ans


# time complexity: O(n^2)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        adj = [list(map(int,input().strip().split())) for _ in range(n)]
        print(Solution().findCircleNum(adj))