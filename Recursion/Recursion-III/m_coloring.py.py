from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def graphColoring(self, n, edges, m):
        graph = [[] for _ in range(n)]
        colors = [0]*n
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def isPossible(u,col):
            for v in graph[u]:
                if(colors[v]==col):return False
            return True
        
        def rec(ind):
            if(ind>=n):return True
            for col in range(1,m+1):
                if(isPossible(ind,col)):
                    colors[ind] = col 
                    if(rec(ind+1)):return True
                    colors[ind] = 0
            return False
        
        return rec(0)
                                
# time complexity: O(m^n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))