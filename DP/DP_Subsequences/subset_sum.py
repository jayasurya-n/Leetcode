from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def isSubsetSum (self, arr, sum):
        n = len(arr)
        dp = [[False]*(sum+1) for _ in range(n)]
        
        for i in range(n):dp[i][0] = True
        if(arr[0]<=sum):dp[0][arr[0]] = True
        
        for i in range(1,n):
            for s in  range(1,sum+1):
                dp[i][s] = dp[i-1][s]
                if(s>=arr[i]):dp[i][s] = dp[i][s] or dp[i-1][s-arr[i]]
        return dp[n-1][sum]
        
# time complexity: O(n*sum)
# space complexity: O(n*sum)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = list(map(int,input().strip().split()))
        sum = int(input().strip())
        print(Solution().isSubsetSum(len(arr),arr,sum))