from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def shortest_distance(self, matrix):
        n = len(matrix)
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if(matrix[i][via]!=-1 and matrix[via][j]!=-1):
                        maxi = matrix[i][j]
                        if matrix[i][j]==-1:maxi = sys.maxsize 
                        matrix[i][j] = min(maxi,matrix[i][via]+matrix[via][j])

# time complexity: O(n^3)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))