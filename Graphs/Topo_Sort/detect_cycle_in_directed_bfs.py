from typing import List,Optional
from collections import deque
import sys
class Solution:
    def isCyclic(self, n : int , adj : List[List[int]]):
        def bfs(start):
            q = deque(start)
            
            while q:
                u = q.popleft()
                self.cnt+=1
                for v in adj[u]:
                    indegree[v]-=1
                    if(indegree[v]==0):q.append(v)
            
        indegree = [0]*n
        for u in range(n):
            for v in adj[u]:
                indegree[v]+=1
                
        start = []
        for u in range(n):
            if(indegree[u]==0):start.append(u)
        
        self.cnt = 0
        bfs(start)
        return self.cnt!=n
# time complexity: O(n+e)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))