class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        # n = len(nums)
        # dict = {}   

        # for i in range(n):
        #     if(nums[i] not in dict):
        #         dict[nums[i]]=1
        #     else:
        #         dict[nums[i]]+=1

        #     if(dict[nums[i]]>n//2):
        #         return nums[i]

        n = len(nums)
        cnt = 0
        ans = -1
        for i in range(n):
            if(cnt==0):
                ans = nums[i]
            if(nums[i]==ans):cnt+=1
            else:cnt-=1
        
        cnt = 0
        for i in range(n):
            if(nums[i]==ans):cnt+=1
        
        if(cnt>(n//2)):return ans




nums = [int(i) for i in input().strip().split()]
obj = Solution()
print(obj.majorityElement(nums))
