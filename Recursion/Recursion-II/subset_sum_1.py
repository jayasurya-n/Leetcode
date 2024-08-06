class Solution:
    def findSubsetsSum(self,index,nums,currentSum,ans):
        if(index==len(nums)):
            ans.append(currentSum)
            return

        self.findSubsetsSum(index+1,nums,currentSum,ans)
        self.findSubsetsSum(index+1,nums,currentSum+nums[index],ans)

    def subsetSums(self, nums, n):
        ans,currentSum = [],0
        self.findSubsetsSum(0,nums,currentSum,ans)
        return ans


nums = list(map(int,input().strip().split()))
print(Solution().subsetSums(nums,len(nums)))