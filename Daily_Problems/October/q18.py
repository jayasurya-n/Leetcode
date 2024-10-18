from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # maxi = 0
        # for num in nums:maxi|=num
        
        # def countSubsets(index,curr):
        #     if(index==len(nums)):
        #         if(curr==maxi):return 1
        #         else:return 0
        #     return countSubsets(index+1,curr)+countSubsets(index+1,curr|nums[index])
        
        # return countSubsets(0,0)
        
        maxi = 0
        for num in nums:maxi|=num
        dp = [[-1]*(maxi+1) for _ in range(len(nums))]
        
        def countSubsets(index,curr):
            if(index==len(nums)):
                if(curr==maxi):return 1
                else:return 0
            
            if(dp[index][curr]!=-1):return dp[index][curr]
            dp[index][curr] = countSubsets(index+1,curr)+countSubsets(index+1,curr|nums[index])
            return dp[index][curr]
        
        return countSubsets(0,0)
        
# time complexity: O(2^n),O(n*maxOR)
# space complexity: O(n),O(n*maxOR)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))