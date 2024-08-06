class Solution:
    def getSubsets(self,i,nums,list,ans):
        if(i==len(nums)):
            ans.append(list.copy())
            return

        list.append(nums[i])
        self.getSubsets(i+1,nums,list,ans)
        list.pop()

        self.getSubsets(i+1,nums,list,ans)

    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans,l = [],[]
        self.getSubsets(0,nums,l,ans)
        return ans

# time complexity: O((2^n)*n)  
# space complexity: O(n)(recursion stack)
nums = list(map(int,input().strip().split()))
print(Solution().subsets(nums))