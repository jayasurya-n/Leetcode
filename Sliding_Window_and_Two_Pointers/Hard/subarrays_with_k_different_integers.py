from typing import List
class Solution:
    def countSubarrays(self,nums,k):
        if(k<=0):return 0
        i,j=0,0
        ans = 0
        hash = dict()
        while(j<len(nums)):
            hash[nums[j]] = hash.setdefault(nums[j],0)+1
            while(len(hash)>k):
                hash[nums[i]]-=1
                if(hash[nums[i]]==0):del hash[nums[i]]
                i+=1
            ans+=j-i+1
            j+=1
        return ans
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.countSubarrays(nums,k) - self.countSubarrays(nums,k-1)


# time complexity: O(2n+2n)
# space complexity: O(n) not O(2n) because same space can be used for next call
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        nums = list(map(int,input().strip().split()))
        k = int(input().strip())
        print(Solution().subarraysWithKDistinct(nums,k))