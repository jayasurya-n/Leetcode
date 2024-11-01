from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        total = sum(arr)//2 
        if(2*total!=sum(arr)):return False
        n = len(arr)
        dp = [[False]*(total+1) for _ in range(n)]
        for i in range(n):dp[i][0] = True
        if(arr[0]<=total):dp[0][arr[0]] = True
        
        for i in range(1,n):
            for s in  range(1,total+1):
                dp[i][s] = dp[i-1][s]
                if(s>=arr[i]):dp[i][s] = dp[i][s] or dp[i-1][s-arr[i]]
        return dp[n-1][total]

# time complexity: O(n*sum)
# space complexity: O(n*sum)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = list(map(int,input().strip().split()))
        print(Solution().canPartition(arr))