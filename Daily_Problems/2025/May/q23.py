from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # n = len(nums)
        # adj = [[] for _ in range(n)]
        # for u,v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)

        # # dp[u][0]: maximum sum of nodes of tree rooted at u with even toggles  
        # # dp[u][1]: maximum sum of nodes of tree rooted at u with odd  toggles  
        # def dfs(u,parent):
        #     dp1,dp2 = nums[u],nums[u]^k
        #     # even,odd
        #     for v in adj[u]:
        #         if(v==parent):continue
        #         c1,c2 = dfs(v,u)

        #         temp1,temp2 = dp1,dp2 
        #         dp1 = max(c1+temp1,c2+temp2) #even+even, odd+odd
        #         dp2 = max(c1+temp2,c2+temp1) #even+odd, odd+even
        #     return dp1,dp2

        # return dfs(0,-1)[0]

        n = len(nums)
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # dp[u][0]: maximum sum of nodes of tree rooted at u with even toggles  
        # dp[u][1]: maximum sum of nodes of tree rooted at u with odd  toggles  
        def dfs(u,parent):
            dp1,dp2 = nums[u],nums[u]^k
            # even,odd
            for v in adj[u]:
                if(v==parent):continue
                c1,c2 = dfs(v,u)

                temp1,temp2 = dp1,dp2 
                dp1 = max(c1+temp1,c2+temp2) #even+even, odd+odd
                dp2 = max(c1+temp2,c2+temp1) #even+odd, odd+even
            return dp1,dp2

        return dfs(0,-1)[0]

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))