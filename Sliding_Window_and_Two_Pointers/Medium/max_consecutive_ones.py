from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # i,j = 0,0
        # ans = 0
        # while(j<len(nums)):
        #     if(nums[j]==0):k-=1
        #     while(k<0):
        #         if(nums[i]==0):k+=1
        #         i+=1
        #     ans = max(ans,j-i+1)
        #     j+=1
        # return ans

        i,j = 0,0
        ans = 0
        while(j<len(nums)):
            if(nums[j]==0):k-=1
            if(k<0):
                if(nums[i]==0):k+=1
                i+=1
            ans = max(ans,j-i+1)
            j+=1
        return ans


# time complexity: O(2n) first case, O(n) in second case
# space complexity: O(1) in both cases 
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        nums = list(map(int,input().strip().split()))
        k = int(input().strip())
        print(Solution().longestOnes(nums,k))