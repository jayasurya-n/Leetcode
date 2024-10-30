from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        
        for j in range(n):dp[0][j] = matrix[0][j]
        dy = [-1,0,1]
        
        for i in range(1,m):
            for j in range(n):
                ans = sys.maxsize
                for k in range(3):
                    nj = j+dy[k]
                    if(nj>=0 and nj<m):ans = min(ans,matrix[i][j]+dp[i-1][nj])
                dp[i][j] = ans
        return min(dp[m-1])

# time complexity: O(mn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        matrix = [list(map(int,input().strip().split())) for _ in range(n)]
        print(Solution().minFallingPathSum(matrix))