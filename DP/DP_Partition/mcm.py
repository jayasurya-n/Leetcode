from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def matrixMultiplication(self, n, arr):
        dp = [[sys.maxsize]*(n) for _ in range(n)]
        for i in range(1,n):dp[i][i]=0
        
        for len in range(2,n):
            for i in range(1,n-len+1):
                j = i+len-1
                for k in range(i,j):
                    cost = arr[i-1]*arr[k]*arr[j]+dp[i][k]+dp[k+1][j]
                    dp[i][j] = min(dp[i][j],cost)
        return dp[1][n-1]
            
# time complexity: O(n^3)
# space complexity: O(n^2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = list(map(int,input().strip().split()))
        print(Solution().matrixMultiplication(len(arr),arr))