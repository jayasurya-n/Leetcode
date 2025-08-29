from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for diff in range(-n+1,n):
            temp = []
            indices = []
            if(diff>0):
                for i in range(n):
                    j = diff+i
                    if(j>=n):break
                    temp.append(grid[i][j])
                    indices.append((i,j))
            else:
                temp = []
                for j in range(n):
                    i = -diff+j
                    if(i>=n):break
                    temp.append(grid[i][j])
                    indices.append((i,j))
            
            temp.sort(reverse=(diff<=0))

            for ind,(i,j) in enumerate(indices):
                grid[i][j] = temp[ind]

        return grid

# time complexity: O(n^2logn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        grid = [lii() for _ in range(n)]
        print(Solution().sortMatrix(grid))