from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # n = len(nums)
        # def check(ones,val):
        #     for k in range(32):
        #         if(val&(1<<k) and ones[k]>0):return False
        #     return True
        
        # ones = [0]*32
        # ans = 0  
        # i,j = 0,0       
        # while(j<n):
        #     while (j>i and check(ones,nums[j])==False):
        #         for k in range(32):
        #             if(nums[i]&(1<<k)):ones[k]-=1
        #         i+=1
            
        #     ans = max(ans,j-i+1)
            
        #     for k in range(32):
        #         if(nums[j]&(1<<k)):ones[k]+=1
        #     j+=1
        
        # return ans
        
        n = len(nums)
        ans = 0
        used = 0
        
        i = j = 0        
        while(j<n):
            while(j>i and used&nums[j]!=0):
                used^=nums[i]
                i+=1
            
            used|=nums[j]
            ans = max(ans,j-i+1)
            j+=1
        
        return ans
                
# time complexity: O(32n),O(n)
# space complexity: O(32),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))