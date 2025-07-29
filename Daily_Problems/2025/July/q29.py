from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # ans = [-1]*n

        # def solve_ones_array(val):
        #     count = [0]*32
        #     for i in range(32):
        #         if((val>>i)&1==1):count[i] = 1
        #     return count
        

        # ones = [0]*32
        # end = n-1
        # or_val = 0
        # for j in range(n-1,-1,-1):
        #     or_val|=nums[j]
        #     count = solve_ones_array(nums[j])
        #     for i in range(32):
        #         ones[i]+=count[i]
            
        #     while end>j:
        #         count = solve_ones_array(nums[end])
        #         ok = True
        #         for i in range(32):
        #             if(ones[i]>0):
        #                 ones[i]-=count[i]
        #                 if(ones[i]<=0):ok = False
                
        #         if(not ok):
        #             for i in range(32):
        #                 ones[i]+=count[i]
        #             break
                
        #         end-=1

        #     ans[j] = end-j+1
        
        # return ans

        n = len(nums)
        ones = [-1]*32
        ans = [-1]*n

        for i in range(n-1,-1,-1):
            end = i
            for bit in range(32):
                if(nums[i]>>bit)&1==1:ones[bit] = i
                else:
                    if(ones[bit]!=-1):end = max(end,ones[bit])
            
            ans[i] = end-i+1
        
        return ans

# time complexity: O(32n),O(32n)
# space complexity: O(32),O(32)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))