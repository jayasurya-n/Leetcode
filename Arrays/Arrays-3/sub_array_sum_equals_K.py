class Solution:

    def subarraySum(self, nums: list[int], k: int) -> int:
        # n = len(nums)
        # cnt = 0

        # for i in range(n):
        #     sum = 0
        #     for j in range(i,n):
        #         sum+=nums[j]
        #         if(sum==k):cnt+=1
        
        # return cnt

        dict = {}
        prefixSum = 0
        cnt = 0 
        dict[prefixSum] = 1

        for i in range(0,len(nums)):
            prefixSum+=nums[i]
            prefixSumEarlier = prefixSum - k

            if(prefixSumEarlier in dict):cnt+=dict[prefixSumEarlier]
            dict[prefixSum]= dict.setdefault(prefixSum,0)+1

        return cnt



k = int(input())
nums = [int(i) for i in input().strip().split()]
obj = Solution()
print(obj.subarraySum(nums,k))
