from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # top sort 
        n = len(colors)
        adj = [[] for _ in range(n)]
        indegree = [0]*n

        for u,v in edges:
            adj[u].append(v)
            indegree[v]+=1
        
        dp = [[0]*26 for _ in range(n)]   
        # dp[u][c]: maximum count of color c ending at u 
        # transition: u->v dp[u][c] = max(dp[u][c],dp[v][c]+color[v]==c)

        q = deque([])
        for u in range(n):
            if(indegree[u]==0):
                q.append(u)
                dp[u][ord(colors[u])-ord('a')]=1
        
        ans = cnt = 0    
        while q:
            u = q.popleft()
            cnt+=1
            for v in adj[u]:
                v_color = ord(colors[v])-ord('a')
                for c in range(26):
                    dp[v][c] = max(dp[v][c],dp[u][c]+(v_color==c))

                indegree[v]-=1
                if(indegree[v]==0):
                    q.append(v)
            ans = max(ans,max(dp[u]))
        
        return ans if cnt==n else -1

# time complexity: O(v+e+26*v)
# space complexity: O(26*v+e)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))