from typing import List,Optional
from collections import deque
import sys
class Solution:
    # def printGraph(self, n : int, edges : List[List[int]]):
    #     adj = [[0]*n for _ in range(n)]
    #     for u,v in edges:
    #         adj[u][v] = 1
    #         adj[v][u] = 1
    #     return adj
    
    def printGraph(self, n : int, edges : List[List[int]]):
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

# time complexity: O(n^2),O(2e)
# space complexity: O(n^2),O(2e)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,e = list(map(int,input().strip().split()))
        edges = [list(map(int,input().strip().split())) for _ in range(e)]
        print(Solution().printGraph(n,edges))