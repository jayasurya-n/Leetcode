class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # cnt0 = 0
        # cnt1 = 0
        # cnt2 = 0

        # for i in range(len(nums)):
        #     if(nums[i]==0):
        #         cnt0+=1
        #     if(nums[i]==1):
        #         cnt1+=1
        #     if(nums[i]==2):
        #         cnt2+=1
        
        # for i in range(len(nums)):
        #     if(i<cnt0):
        #         nums[i] = 0
        #     elif(cnt0<=i<cnt1+cnt0):
        #         nums[i] = 1
        #     else:
        #         nums[i] = 2
        # return nums


        n = len(nums)
        low = 0
        mid = 0
        high = n-1

        while(mid<=high):
            if(nums[mid]==0):
                nums[low],nums[mid] = nums[mid],nums[low]
                low+=1
                mid+=1
            elif(nums[mid]==1):mid+=1
            else:
                nums[mid],nums[high] = nums[high], nums[mid]
                high-=1


nums = [int(x) for x in input().strip().split()]
obj = Solution()
print(obj.sortColors(nums))