from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sum = cnt = 0
        small = 10**10
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ele = matrix[i][j]
                sum+=abs(ele)
                small = min(small,abs(ele))
                if(ele<0):cnt+=1
        
        if(cnt%2==0):return sum
        return sum-2*small

# time complexity: O(mn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))