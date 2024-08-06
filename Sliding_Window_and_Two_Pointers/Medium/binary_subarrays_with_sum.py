from typing import List
class Solution:
    def countSubarrays(self,nums,goal):
        if(goal<0):return 0
        i,j=0,0
        ans=0
        sum=0
        while(j<len(nums)):
            sum+=nums[j]
            while(sum>goal):
                if(nums[i]==1):sum-=1
                i+=1
            ans+=j-i+1
            j+=1
        return ans

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.countSubarrays(nums,goal)-self.countSubarrays(nums,goal-1)
        

            


# time complexity: O(2n+2n)
# space complexity: O(1)
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        nums = list(map(int,input().strip().split()))
        goal = int(input().strip())
        print(Solution().numSubarraysWithSum(nums,goal))