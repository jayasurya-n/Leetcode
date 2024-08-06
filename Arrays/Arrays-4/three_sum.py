class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
       
        # n = len(nums)
        # ans = set() 

        # for i in range(n-1):
        #     hashSet = set()
        #     for j in range(i+1,n):
        #         third = -(nums[i]+nums[j])
        #         if(third in hashSet):
        #             l = [nums[i],nums[j],third]
        #             l.sort()
        #             ans.add(tuple(l))
        #         hashSet.add(nums[j])

        # return [list(i) for i in ans]

        n = len(nums)
        nums.sort()
        ans = []

        for i in range(0,n-2):
            if(i>0 and nums[i]==nums[i-1]):continue
            
            j = i+1
            k = n-1
            while(j<k):
                sum = nums[i]+nums[j]+nums[k] 
                if(sum==0):
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1

                    while(j<k and nums[j]==nums[j-1]):j+=1
                    while(j<k and nums[k]==nums[k+1]):k-=1

                elif (sum<0):j+=1
                else:k-=1
        
        return ans


nums = [int(i) for i in input().strip().split()]
obj = Solution()
print(obj.threeSum(nums))