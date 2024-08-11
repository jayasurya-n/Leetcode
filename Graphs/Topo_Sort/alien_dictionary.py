from typing import List,Optional
from collections import deque
import sys,math
class Solution:
    def findOrder(self,alien_dict, n, k):
        adj = [[] for _ in range(k)]
        
        for p in range(len(alien_dict)-1):
            cur = alien_dict[p]
            next = alien_dict[p+1]
            i,j = 0,0
            while(i<len(cur) and j<len(next) and cur[i]==next[j]):
                i+=1
                j+=1
            if(i<len(cur) and j<len(next)):
                adj[ord(cur[i])-97].append(ord(next[j])-97)
        
        def bfs(start):
            q = deque(start)
            while q:
                u = q.popleft()
                ans.append(u)
                for v in adj[u]:
                    indegree[v]-=1
                    if(indegree[v]==0):q.append(v)
               
        indegree = [0]*k
        for u in range(k):
            for v in adj[u]:
                indegree[v]+=1 
                    
        start = []
        for u in range(k):
            if(indegree[u]==0):start.append(u)

        ans = []
        bfs(start)
        for i in range(len(ans)):
            ans[i] = chr(ans[i]+97)
        return ans
    
# time complexity: O(n*(len(word)+k))
# space complexity: O(k)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,k = list(map(int,input().strip().split()))
        alien_dict = input().strip().split()
        print(Solution().findOrder(alien_dict,n,k))