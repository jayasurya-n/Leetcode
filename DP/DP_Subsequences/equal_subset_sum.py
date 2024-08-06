from typing import List,Optional
import sys
class Solution:
    # def findSubset(self,index,sum,arr,dp):
    #     if(sum==0):return True
    #     if(index==len(arr)-1): return sum==arr[index]
    #     if(sum<0):return False

    #     if(dp[index][sum]!=-1):return dp[index][sum] 
    #     dp[index][sum] = (self.findSubset(index+1,sum-arr[index],arr,dp) or
    #                         self.findSubset(index+1,sum,arr,dp))
    #     return dp[index][sum]

    # def canPartition(self, arr: List[int]) -> bool:
    #     n = len(arr)
    #     maxSum = 0
    #     for i in arr:maxSum+=i
    #     if(maxSum%2==1):return False

    #     sum = maxSum//2
    #     dp = [[-1]*(sum+1) for _ in range(len(arr))]
    #     return self.findSubset(0,sum,arr,dp)
    
    # def canPartition(self, arr: List[int]) -> bool:
    #     n = len(arr)
    #     maxSum = 0
    #     for i in arr:maxSum+=i
    #     if(maxSum%2==1):return False

    #     sum = maxSum//2
    #     dp = [[False]*(sum+1) for _ in range(len(arr))]

    #     for i in range(len(arr)):dp[i][0] = True
    #     if(arr[0]<=sum):dp[0][arr[0]] = True 

    #     for ind in range(1,len(arr)):
    #         for target in range(1,sum+1):
    #             notTake = dp[ind-1][target]
    #             take = False
    #             if(arr[ind]<=target):take = dp[ind-1][target-arr[ind]]
    #             dp[ind][target] = take or notTake
    #     return dp[n-1][sum]

    def canPartition(self, arr: List[int]) -> bool:
        n = len(arr)
        maxSum = 0
        for i in arr:maxSum+=i
        if(maxSum%2==1):return False

        sum = maxSum//2
        prev = [False]*(sum+1)
        for i in range(len(arr)):prev[0] = True
        if(arr[0]<=sum):prev[arr[0]] = True 

        for ind in range(1,len(arr)):
            curr = [False]*(sum+1)
            curr[0] = True
            for target in range(1,sum+1):
                notTake = prev[target]
                take = False
                if(arr[ind]<=target):take = prev[target-arr[ind]]
                curr[target] = take or notTake
            prev = curr
        return prev[sum]

    

# time complexity: O(n*sum), O(n*sum),O(n*sum)
# space complexity: O(n*sum+n(stack space)), O(n*sum),O(sum)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        arr = list(map(int,input().strip().split()))
        print(Solution().canPartition(arr))