class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        # n = len(nums)
        # dict = {}   

        # for i in range(n):
        #     if(nums[i] not in dict):
        #         dict[nums[i]]=1
        #     else:
        #         dict[nums[i]]+=1


        # l = []
        # for key,value in dict.items():
        #     if(value>n//3):
        #         l.append(key)

        # return l


        n = len(nums)
        cnt1, cnt2 = 0,0
        l1,l2 = -1e10,-1e10

        for i in range(n):
            if(cnt1==0 and nums[i]!=l2):l1 = nums[i]
            elif(cnt2==0 and nums[i]!=l1):l2 = nums[i]

            if(nums[i]==l1):cnt1+=1
            elif(nums[i]==l2):cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        
        cnt1,cnt2 = 0,0
        l = []
        for i in range(n):
            if(nums[i]==l1):cnt1+=1
            if(nums[i]==l2):cnt2+=1
        
        if(cnt1>n//3):l.append(l1)
        if(cnt2>n//3):l.append(l2)
        l.sort()
        return l
            





nums = [int(i) for i in input().strip().split()]
obj = Solution()
print(obj.majorityElement(nums))
