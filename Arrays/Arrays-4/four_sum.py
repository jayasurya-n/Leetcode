class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
       

        n = len(nums)
        dict = {}

        for i in range(n):
            diff = target-nums[i]
            if(diff not in dict):
                dict[nums[i]] = i
            else:
                return [i,dict[diff]]
            
            

       
        
        return ans
        

            



target = int(input())
nums = [int(i) for i in input().strip().split()]
obj = Solution()
print(obj.twoSum(nums,target))