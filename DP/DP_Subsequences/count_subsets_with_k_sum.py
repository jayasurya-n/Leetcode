from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def perfectSum(self, arr, n, sum):
        dp = [[0]*(sum+1) for _ in range(n)]
        
        for i in range(n):dp[i][0] = 1
        if(arr[0]<=sum):dp[0][arr[0]]+=1
        
        for i in range(1,n):
            for s in  range(0,sum+1):
                dp[i][s] = dp[i-1][s]
                if(s>=arr[i]):dp[i][s]=(dp[i][s]+dp[i-1][s-arr[i]])%(10**9+7)
        return dp[n-1][sum]
        
# time complexity: O(n*sum)
# space complexity: O(n*sum)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,sum = list(map(int,input().strip().split()))
        arr = list(map(int,input().strip().split()))
        print(Solution().perfectSum(arr,n,sum))