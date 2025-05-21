from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # m,n = len(matrix),len(matrix[0])
        # row_col = [0]*(m+n)
        # for i in range(m):
        #     for j in range(n):
        #         if(matrix[i][j]==0):
        #             row_col[i] = 1
        #             row_col[j+m] = 1
        
        # for k in range(m+n):
        #     if(row_col[k]==0):continue
        #     if(k<m):
        #         for j in range(n):
        #             matrix[k][j] = 0
        #     else:
        #         for i in range(m):
        #             matrix[i][k-m] = 0

        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]==0):
                    for k in range(n):
                        if(matrix[i][k]!=0):
                            matrix[i][k] = None
                    break
        
        for j in range(n):
            for i in range(m):
                if(matrix[i][j]==0):
                    for k in range(m):
                        matrix[k][j] = None
                    break        
        
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]==None):
                    matrix[i][j] = 0

# time complexity: O(mn+m+n),O(mn)
# space complexity: O(m+n),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))