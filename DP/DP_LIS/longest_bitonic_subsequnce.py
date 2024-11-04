from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq,bisect

class Solution:
    # def LongestBitonicSequence(self, n : int, nums : List[int]) -> int:
    #     dp1 = [1]*n
    #     dp2 = [1]*n
        
    #     for i in range(1,n):
    #         for j in range(i):
    #             if(nums[j]<nums[i]):
    #                 dp1[i] = max(dp1[i],1+dp1[j])
        
    #     for i in range(n-1,-1,-1):
    #         for j in range(i+1,n):
    #             if(nums[j]<nums[i]):
    #                 dp2[i] = max(dp2[i],1+dp2[j])
        
    #     ans=0
    #     for i in range(n):
    #         if(dp1[i]>1 and dp2[i]>1):
    #             ans = max(ans,dp1[i]+dp2[i]-1)
    #     return ans
    
    def LongestBitonicSequence(self, n : int, nums : List[int]) -> int:
        def _lis(nums):
            lis = [0]*n
            ans = []
            for i in range(n):
                pos = bisect.bisect_left(ans,nums[i])
                if(pos==len(ans)):ans.append(nums[i])
                else:ans[pos] = nums[i]
                lis[i] = pos+1
            return lis
        
        lis = _lis(nums)
        lds = _lis(nums[::-1])[::-1]
        
        ans=0
        for i in range(n):
            if(lis[i]>1 and lds[i]>1):
                ans = max(ans,lis[i]+lds[i]-1)
        return ans
# time complexity: O(n^2),O(nlogn)
# space complexity: O(n),O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))