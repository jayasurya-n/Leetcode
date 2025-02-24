from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges)+1
        adj = [[] for _ in range(n)]
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bob_dfs(u,parent,time):
            self.bob_path[u] = time
            if(u==0):return True
            
            for v in adj[u]:
                if(v==parent):continue
                if(bob_dfs(v,u,time+1)):return True
            
            self.bob_path.pop(u)
            return False
        
        self.bob_path = defaultdict(int)
        bob_dfs(bob,-1,0)
    
        def alice_dfs(u,parent,time,csum):
            if(u not in self.bob_path):csum+=amount[u]
            elif(self.bob_path[u]>time):csum+=amount[u]
            elif(self.bob_path[u]==time):csum+=amount[u]//2
            
            if(len(adj[u])==1 and u!=0):self.ans = max(self.ans,csum)
            
            for v in adj[u]:
                if(v==parent):continue
                alice_dfs(v,u,time+1,csum)
        
        self.ans = -10**18
        alice_dfs(0,-1,0,0)
        return self.ans
            
# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))