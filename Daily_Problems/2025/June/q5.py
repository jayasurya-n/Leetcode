from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class DisjointSet:
    def __init__(self,n):
        self.parent = list(range(n+1))

    def findUltimateParent(self,u):
        if(u==self.parent[u]):return u
        self.parent[u] = self.findUltimateParent(self.parent[u])
        return self.parent[u]

    def unionbyRank(self,u,v):
        pu = self.findUltimateParent(u)
        pv = self.findUltimateParent(v)
        if(pu==pv):return

        if(pu<pv):self.parent[pv] = pu
        else:self.parent[pu] = pv

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # adj = [set() for _ in range(26)]
        # for ch1,ch2 in zip(s1,s2):
        #     adj[ord(ch1)-97].add(ord(ch2)-97)
        #     adj[ord(ch2)-97].add(ord(ch1)-97)
        
        # def dfs(u,visited):
        #     visited[u] = True
        #     ans = u
        #     for v in adj[u]:
        #         if(visited[v]):continue
        #         ans = min(ans,dfs(v,visited))
        #     return ans

        # def initilaize(u,visited,parent,smallest):
        #     visited[u] = True
        #     parent[u] = smallest
        #     for v in adj[u]:
        #         if(visited[v]):continue
        #         initilaize(v,visited,parent,smallest)

        # visited1 = [False]*26
        # visited2 = [False]*26
        # parent = [None]*26
        # for u in range(26):
        #     if(not visited1[u]):
        #         smallest = dfs(u,visited1)
        #         initilaize(u,visited2,parent,smallest)
        
        # ans = []
        # for i in range(len(baseStr)):
        #     smallest_char = parent[ord(baseStr[i])-97]
        #     ans.append(chr(smallest_char+97))
        # return "".join(ans)

        ds = DisjointSet(26)
        for ch1,ch2 in zip(s1,s2):
            ds.unionbyRank(ord(ch1)-97,ord(ch2)-97)
        
        ans = []
        for i in range(len(baseStr)):
            smallest_char = ds.findUltimateParent(ord(baseStr[i])-97)
            ans.append(chr(smallest_char+97))
        return "".join(ans)

# time complexity: O(n+m),O(n+m)
# space complexity: O(26),O(26)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))