from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        ans = 0
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]==1):
                    dp[i+1][j+1] = 1+min(dp[i][j+1],dp[i+1][j],dp[i][j])
                    ans+=dp[i+1][j+1]
        return ans
                
# time complexity: O(mn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        matrix = list(map(int,input().strip().split()))
        print(Solution().countSquares(matrix))