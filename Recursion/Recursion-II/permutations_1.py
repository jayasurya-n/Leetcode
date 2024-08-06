class Solution:
    # def findPermutations(self,nums,freq,store,ans):
    #     if(len(store)==len(nums)):
    #         ans.append(store[:])
    #         return
        
    #     for i in range(len(nums)):
    #         if(freq[i]==0):
    #             freq[i] = 1
    #             self.findPermutations(nums,freq,store+[nums[i]],ans)
    #             freq[i] = 0

    # def permute(self, nums: list[int]) -> list[list[int]]:
    #     freq = [0 for i in nums]
    #     store,ans = [],[]
    #     self.findPermutations(nums,freq,store,ans)
    #     return ans

    def findPermutations(self,index,nums,ans):
        if(index==len(nums)):
            ans.append(nums[:])
            return
        
        for i in range(index,len(nums)):
            nums[index],nums[i] = nums[i],nums[index]
            self.findPermutations(index+1,nums,ans)
            nums[index],nums[i] = nums[i],nums[index]

    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        index = 0
        self.findPermutations(index,nums,ans)
        return ans



# time complexity: O(n!*n)  
# space complexity: O(n)(stack space) 
nums = list(map(int,input().strip().split()))
print(Solution().permute(nums))