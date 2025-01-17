from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for i in range(n-1):graph[i].append(i+1)
        
        def shortestDistance(s,t,graph):
            q = deque([s])
            visited = {s}
            level = 0
            
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    if(node==t):return level
                    
                    for v in graph[node]:
                        if v not in visited:
                            visited.add(v)
                            q.append(v)
                level+=1
            return level
                    
        ans = []
        for u,v in queries:
            graph[u].append(v)
            ans.append(shortestDistance(0,n-1,graph))
        return ans

# time complexity: O(q(n+q))
# space complexity: O(n+q)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))