from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        ans = [0]*n
        
        i,j = 0,n-1
        l,r = 0,n-1
        while(i<n):
            if(nums[i]<pivot):
                ans[l] = nums[i]
                l+=1
            
            if(nums[j]>pivot):
                ans[r] = nums[j]
                r-=1

            i+=1
            j-=1
        
        while(l<=r):
            ans[l] = pivot
            l+=1
        
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))