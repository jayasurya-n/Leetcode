class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow,fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if(slow==fast):
                break
        
        slow = 0

        while (slow!=fast):
            slow = nums[slow]
            fast = nums[fast]
        
        return slow


        

nums = [int(x) for x in input().strip().split()]
obj = Solution()
print(obj.findDuplicate(nums))