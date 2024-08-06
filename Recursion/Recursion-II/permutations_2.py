class Solution:
    # def findPermutations(self,nums,freq,store,ans):
    #     if(len(store)==len(nums)):
    #         ans.append(store[:])
    #         return
        
    #     for i in range(len(nums)):
    #         if(freq[i]==0):
    #             if (i>0 and nums[i]==nums[i-1] and freq[i-1]==1):continue
    #             freq[i] = 1
    #             self.findPermutations(nums,freq,store+[nums[i]],ans)
    #             freq[i] = 0

    # def permuteUnique(self, nums: list[int]) -> list[list[int]]:
    #     freq = [0 for i in nums]
    #     store,ans = [],[]
    #     nums.sort()
    #     self.findPermutations(nums,freq,store,ans)
    #     return ans

    def findPermutations(self,index,nums,ans):
        if(index==len(nums)):
            ans.append(nums[:])
            return
        
        hash = set()
        for i in range(index,len(nums)):
            if(nums[i] in hash):continue
            hash.add(nums[i])
            nums[index],nums[i] = nums[i],nums[index]
            self.findPermutations(index+1,nums,ans)
            nums[index],nums[i] = nums[i],nums[index]

    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans = []
        index = 0
        nums.sort()
        self.findPermutations(index,nums,ans)
        return ans


# time complexity: O(n!*n)  
# space complexity: O(n)(stack sapce)
nums = list(map(int,input().strip().split()))
print(Solution().permuteUnique(nums))