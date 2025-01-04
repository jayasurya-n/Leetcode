from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def findDiameter(edges):
            m = len(edges)+1
            graph = [[] for _ in range(m)] 
            for u,v in edges:
                graph[u].append(v)
                graph[v].append(u)
            
            def dfs(u,parent):
                farthest_node = u
                maxi = 0
                
                for v in graph[u]:
                    if v!=parent:
                        dist,far_node = dfs(v,u)
                        if(1+dist>maxi):
                            maxi = 1+dist
                            farthest_node = far_node
                return maxi,farthest_node

            _,farthest_from_start = dfs(0,-1)
            diameter,_ = dfs(farthest_from_start,-1)
            return diameter
        
        d1 = findDiameter(edges1)
        d2 = findDiameter(edges2)
        
        return max(d1,d2,math.ceil(d1/2)+math.ceil(d2/2)+1)

# time complexity: O(m+n)
# space complexity: O(m+n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))