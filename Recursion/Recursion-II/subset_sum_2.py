class Solution:
    def findsubSets(self,start,nums,store,ans):
        ans.append(store[:])
        for i in range(start,len(nums)):
            if(i>start and nums[i]==nums[i-1]):continue
            self.findsubSets(i+1,nums,store+[nums[i]],ans)

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans,store,start = [],[],0
        nums.sort()
        self.findsubSets(start,nums,store,ans)
        return ans


nums = list(map(int,input().strip().split()))
print(Solution().subsetsWithDup(nums))