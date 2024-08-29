from typing import List,Optional
from collections import deque
import sys, math, heapq

class DisjointSet:
    
    def __init__(self,n):
        self.rank = [0]*(n+1)
        self.parent = [0]*(n+1)
        for i in range(n+1):self.parent[i] = i
    
    def findUltimateParent(self,u):
        if(u==self.parent[u]):return u
        self.parent[u] = self.findUltimateParent(self.parent[u])
        return self.parent[u]

    def unionbyRank(self,u,v):
        ulp_u = self.findUltimateParent(u) 
        ulp_v = self.findUltimateParent(v)
        
        if(ulp_u==ulp_v):return 
        
        rank_u = self.rank[ulp_u] 
        rank_v = self.rank[ulp_v]
        
        if(rank_u < rank_v):self.parent[ulp_u] = ulp_v
        elif(rank_u > rank_v):self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u]+=1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]):
        n = len(accounts)
        hash = dict()
        ds = DisjointSet(n)
        for i in range(n):
            for j in range(1,len(accounts[i])): 
                email = accounts[i][j]
                if(email not in hash):hash[email] = i
                else:
                    node = hash[email]
                    ds.unionbyRank(node,i)
        
        ans = [[] for _ in range(n)]
        for email,ind in hash.items():
            parent = ds.findUltimateParent(ind)
            ans[parent].append(email)

        
        final = []
        for i in range(n):
            if(ans[i]!=[]):
                l = sorted(ans[i])
                l.insert(0,accounts[i][0])
                final.append(l)
        return final
                    
# time complexity: O(varies from input)
# space complexity: O(varies from input)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        accounts = [input().strip().split() for _ in range(n)]
        print(Solution().accountsMerge(accounts=accounts))