from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # mod = 10**9+7
        # adj = [[] for _ in range(n)]
        # for u,v,t in roads:
        #     adj[u].append((v,t))
        #     adj[v].append((u,t))
        
        # time = [10**18]*n
        # time[0] = 0
        
        # pq = [(0,0)]
        # while pq:
        #     t,u = heapq.heappop(pq)
        #     for v,nt in adj[u]:
        #         if(time[v]>t+nt):
        #             time[v] = t+nt
        #             heapq.heappush(pq,(t+nt,v))
        
        # # order = sorted(range(n), key=lambda x: time[x],reverse=True)
        # # dp = [0]*n
        # # dp[n-1] = 1
        
        # # for u in order:
        # #     for v,t in adj[u]:
        # #         if(time[u]+t==time[v]):
        # #             dp[u]+=dp[v]
        # #             dp[u]%=mod
        # # return dp[0]
        
        # memo = {n-1:1}
        # def dfs(u):
        #     if(u in memo):return memo[u]
        #     ans = 0
        #     for v,t in adj[u]:
        #         if(time[u]+t==time[v]):
        #             ans+=dfs(v)
        #             ans%=mod
        #     memo[u] = ans
        #     return ans

        # return dfs(0)
        
        mod = 10**9+7
        adj = [[] for _ in range(n)]
        for u,v,t in roads:
            adj[u].append((v,t))
            adj[v].append((u,t))
        
        time = [10**18]*n
        time[0] = 0
        
        dp = [0]*n
        dp[0] = 1
        
        pq = [(0,0)]
        while pq:
            t,u = heapq.heappop(pq)
            for v,nt in adj[u]:
                if(time[v]>t+nt):
                    time[v] = t+nt
                    dp[v] = dp[u] 
                    heapq.heappush(pq,(t+nt,v))
                elif(time[v]==t+nt):
                    dp[v]+=dp[u]
                    dp[v]%=mod
        
        return dp[n-1]
        
# time complexity: O((e+v)logv),O((e+v)logv)
# space complexity: O(v+e),O(v+e)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))