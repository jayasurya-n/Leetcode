from typing import List
import sys
class Solution:
    # def minDifference(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     if(n<=4):return 0
    #     nums.sort()
    #     ans = max(nums)-min(nums)
    #     ans = min(ans,nums[n-4]-nums[0])
    #     ans = min(ans,nums[n-1]-nums[3])
    #     ans = min(ans,nums[n-2]-nums[2])
    #     ans = min(ans,nums[n-3]-nums[1])
    #     return ans
    
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if(n<=4):return 0
        for i in range(0,4):
            for j in range(0,n-i-1):
                if(nums[j]>nums[j+1]):nums[j],nums[j+1] = nums[j+1],nums[j]
            # print("BubbleSort Maximum:",nums)
            
            for j in range(n-2,i-1,-1):
                if(nums[j]>nums[j+1]):nums[j],nums[j+1] = nums[j+1],nums[j]
            # print("BubbleSort Minimum:",nums)
        
        ans = max(nums)-min(nums)
        ans = min(ans,nums[n-4]-nums[0])
        ans = min(ans,nums[n-1]-nums[3])
        ans = min(ans,nums[n-2]-nums[2])
        ans = min(ans,nums[n-3]-nums[1])
        return ans
        


        
# time complexity: O(nlogn) in first, O(n) in second 
# space complexity: O(1) in both
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        nums = list(map(int,input().strip().split()))
        print(Solution().minDifference(nums))