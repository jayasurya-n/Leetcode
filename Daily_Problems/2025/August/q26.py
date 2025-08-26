from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = area = 0
        for l,w in dimensions:
            diag = l**2+w**2
            if(diag>max_diag):
                area = l*w
                max_diag = diag
            elif(diag==max_diag):area = max(area,l*w)
        return area

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))