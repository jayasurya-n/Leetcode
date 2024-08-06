class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        pass
        n = len(nums)
        max = -1e5
        sum = 0
        start = -1
        stop = -1

        for i in range(0,n):
            if(sum==0):start_i = i
            sum +=nums[i]
            if(sum>max):
                max = sum
                start = start_i
                stop = i
            if(sum<0):
                sum = 0

        return max,start,stop



nums = [int(x) for x in input().strip().split()]
obj = Solution()
print(obj.maxSubArray(nums))