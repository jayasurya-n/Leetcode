from typing import List,Optional
import sys
class Solution:
    def countPartitions(self, n : int, d : int, arr : List[int]) -> int:
        totalSum = sum(arr)
        if((totalSum+d)%2==1):return 0
        if(d>totalSum):return 0
        target = (totalSum-d)//2

        mod = 10**9+7
        dp = [[0]*(target+1) for _ in range(n)]

        for i in range(n):dp[i][0] = 1
        if(arr[0]<=target):
            if(arr[0]==0):dp[0][arr[0]]=2
            else:dp[0][arr[0]] = 1

        for i in range(1,n):
            for s in range(0,target+1):
                dp[i][s] = dp[i-1][s]
                if(arr[i]<=s):
                    dp[i][s] = (dp[i-1][s] + dp[i-1][s-arr[i]])%mod

        return dp[n-1][target]


# time complexity: O(n^2)
# space complexity: O(n^2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,d = list(map(int,input().strip().split()))
        arr = list(map(int,input().strip().split()))
        print(Solution().countPartitions(n,d,arr))