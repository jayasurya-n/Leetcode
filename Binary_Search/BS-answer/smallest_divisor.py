import math
class Solution:

    def value(self,nums,divisor):
        sum = 0
        for i in nums:
            sum+=math.ceil(i/divisor)
        return sum
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        low = 1
        high = max(nums)
        ans = 1e8

        while(low<=high):
            mid = (low+high)//2
            
            if(self.value(nums,mid)<=threshold):
                ans = min(mid,ans)
                high = mid-1
            else:
                low = mid+1

        return ans  


    

m,k = [int(i) for i in input().strip().split()]
nums = [int(i) for i in input().strip().split(",")]
obj = Solution()
print(obj.smallestDivisor(nums,threshold))