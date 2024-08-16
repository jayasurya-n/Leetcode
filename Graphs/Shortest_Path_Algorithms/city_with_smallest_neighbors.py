from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int):
        matrix = [[sys.maxsize]*n for _ in range(n)]
        for i in range(n):matrix[i][i] = 0
        
        for u,v,w in edges:
            matrix[u][v] = w
            matrix[v][u] = w    
        
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j],matrix[i][via]+matrix[via][j])
        
        for i in matrix:
            print(i)
        ans = -1
        mini = sys.maxsize
        for i in range(n):
            cnt = 0
            for j in range(n):
                if(matrix[i][j]<=distanceThreshold):cnt+=1
            
            if(mini>cnt or (mini==cnt and i>ans)):
                mini = cnt
                ans = i
        return ans
            
# time complexity: O(n^3)
# space complexity: O(n^3)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,distanceThreshold = list(map(int,input().strip().split()))
        edges = [list(map(int,input().strip().split())) for _ in range(n)]
        print(Solution().findTheCity(n,edges,distanceThreshold))