from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def maximumPoints(self, arr, n):
        s = 3
        dp = [[0]*s for _ in range(n)]
        for j in range(s):dp[0][j] = arr[0][j]
        for i in range(1,n):
            for j in range(s):
                for k in range(s):
                    if(j!=k):dp[i][j] = max(dp[i][j],dp[i-1][k]+arr[i][j])
        return max(dp[n-1])

# time complexity: O(ns^2)
# space complexity: O(ns)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        points = [list(map(int,input().strip().split())) for _ in range(n)]
        print(Solution().maximumPoints(points,n))