from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # def count(nums1,nums2,mid):
        #     def bisectIndex(nums,target,left):
        #         low,high = 0,len(nums)-1
        #         while(low<=high):
        #             mid = (low+high)>>1
        #             if(nums[mid]>target or 
        #             (left and nums[mid]==target)):high = mid-1
        #             else:low = mid+1
        #         return low

        #     ans = 0
        #     for x in nums1:
        #         if(x>0):ans+=bisectIndex(nums2,math.floor(mid/x),left=False)
        #         elif(x<0):ans+=len(nums2)-bisectIndex(nums2,math.ceil(mid/x),left=True)
        #         else:ans+=len(nums2) if mid>=0 else 0
        #     return ans
        
        # low,high = -10**10,10**10
        # while(low<=high):
        #     mid = (low+high)>>1
        #     if(count(nums1,nums2,mid)>=k):high = mid-1
        #     else:low = mid+1
        # return low


        def count(nums1,nums2,mid):
            ans = 0
            for x in nums1:
                if(x>0):ans+=bisect.bisect_right(nums2,math.floor(mid/x))
                elif(x<0):ans+=len(nums2)-bisect.bisect_left(nums2,math.ceil(mid/x))
                else:ans+=len(nums2) if mid>=0 else 0
            return ans
        
        low,high = -10**10,10**10
        while(low<=high):
            mid = (low+high)>>1
            if(count(nums1,nums2,mid)>=k):high = mid-1
            else:low = mid+1
        return low

# time complexity: O(n1logn2logR)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))