from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # n = len(nums)
        # nums.sort()
        
        # def bsIndex(nums,target,index):
        #     # works like bisect.left
        #     # if target is lesser than smallest then index=0
        #     # if target is larger than largest  then index=n
        #     low,high = index,len(nums)-1
        #     while(low<=high):
        #         mid = (low+high)>>1
        #         if(nums[mid]>=target):high = mid-1
        #         else:low = mid+1
        #     return low

        # ans = 0
        # for i in range(n):
        #     cnt =  bsIndex(nums,upper-nums[i]+1,i+1)
        #     cnt-= bsIndex(nums,lower-nums[i],i+1)
        #     ans+=cnt
        # return ans


        n = len(nums)
        nums.sort()
        
        def countPairs(target):
            # pairs that are <=target
            i,j = 0,n-1
            cnt = 0
            
            while(i<j):
                if(nums[i]+nums[j]<=target):
                    cnt+=j-i
                    i+=1
                else:j-=1
            return cnt
        
        return countPairs(upper)-countPairs(lower-1)
    
# time complexity: O(nlogn),O(nlogn)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))