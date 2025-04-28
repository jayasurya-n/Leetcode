from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # psum = [0]*(n+1)
        # for i in range(1,n+1):
        #     psum[i] = psum[i-1]+nums[i-1] 
        
        # def bsIndex(nums,target,start):
        #     low,high = start,len(nums)-1
        #     while(low<=high):
        #         mid = (low+high)>>1
        #         val = (psum[mid+1]-psum[start])*(mid-start+1)
        #         if(val>=k):high = mid-1
        #         else:low = mid+1
        #     return high
        
        # ans = 0
        # for i in range(n):
        #     ans+=bsIndex(nums,k,i)-i+1
        # return ans
        
        n = len(nums)
        ans = csum = 0
        i = j = 0 
        for j in range(n):
            csum+=nums[j]
            while(csum*(j-i+1)>=k):
                csum-=nums[i]
                i+=1
            ans+=j-i+1
        return ans

# time complexity: O(nlogn),O(n)
# space complexity: O(n),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        nums = lii()
        k = ii()
        print(Solution().countSubarrays(nums,k))