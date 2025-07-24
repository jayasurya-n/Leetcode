from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(u,par):
            xor_values[u] = nums[u]
            tin[u] = self.timer
            self.timer+=1

            for v in adj[u]:
                if(v==par):continue
                xor_values[u]^=dfs(v,u)

            tout[u] = self.timer
            return xor_values[u]

        xor_values = [0]*n
        tin = [-1]*n
        tout = [-1]*n
        self.timer = 0
        dfs(0,-1)
        total_xor = xor_values[0]
        
        ans = 1<<32
        for u in range(1,n):
            for v in range(u+1,n):
                if(tin[u]<tin[v]<tout[u]):
                    xor1 = xor_values[v]
                    xor2 = xor_values[v]^xor_values[u]

                elif(tin[v]<tin[u]<tout[v]):
                    xor1 = xor_values[u]
                    xor2 = xor_values[u]^xor_values[v]

                else:
                    xor1 = xor_values[u]
                    xor2 = xor_values[v]

                xor3 = total_xor^xor1^xor2
                ans = min(ans,max(xor1,xor2,xor3)-min(xor1,xor2,xor3))
        
        return ans

# time complexity: O(n^2)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))