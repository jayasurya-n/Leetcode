class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        prefix, suffix = 1,1
        ans = -1e10
        for i in range(len(nums)):
            if(prefix==0):prefix=1
            if(suffix==0):suffix=1
            prefix*=nums[i] 
            suffix*=nums[len(nums)-i-1]
            ans = max(ans, max(prefix,suffix))
        return ans



nums = list(map(int,input().strip().split()))
print(Solution().maxProduct(nums))