from typing import List
class Solution:
    def countSubarrays(self,nums,k):
        if(k<0):return 0
        odd = 0
        ans = 0
        i,j = 0,0
        while(j<len(nums)):
            if(nums[j]%2):odd+=1
            while(odd>k):
                if(nums[i]%2):odd-=1
                i+=1
            ans+=j-i+1
            j+=1
        return ans
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.countSubarrays(nums,k)-self.countSubarrays(nums,k-1)
        

            


# time complexity: O(2n+2n)
# space complexity: O(1)
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        nums = list(map(int,input().strip().split()))
        k = int(input().strip())
        print(Solution().numberOfSubarrays(nums,k))