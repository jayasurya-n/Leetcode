from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        self.ans = 0
        def dfs(u,parent):
            sum = 0
            for v in graph[u]:
                if(v!=parent):sum+=dfs(v,u)
            
            sum+=values[u]
            sum%=k
            if(sum==0):self.ans+=1
            return sum
            
        dfs(0,-1)
        return self.ans

# time complexity: O(m+n)
# space complexity: O(m+n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))