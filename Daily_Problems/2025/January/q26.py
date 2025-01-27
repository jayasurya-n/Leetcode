from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indegree = [0]*n
        depth = [1]*n
        
        for u in range(n):indegree[favorite[u]]+=1
        
        q = deque([])
        for i in range(n):
            if(indegree[i]==0):q.append(i)
        
        while q:
            u = q.popleft()
            v = favorite[u]
            depth[v] = max(depth[v],depth[u]+1)
            indegree[v]-=1
            if(indegree[v]==0):q.append(v)
        
        max_cycle = two_cycle = 0 
        for u in range(n):
            if(indegree[u]==0):continue
            cycle = 0
            curr = u
            while indegree[curr]!=0:
                indegree[curr]=0
                cycle+=1
                curr = favorite[curr]
            
            if(cycle==2):two_cycle+=depth[u]+depth[favorite[u]]
            else:max_cycle = max(max_cycle,cycle)
        return max(max_cycle,two_cycle)

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))