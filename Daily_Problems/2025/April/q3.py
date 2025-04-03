from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # n = len(nums)
        # i,j = 0,1
        # imax,jmin = 0,10**7
        # max_diff = 0
        # ans = 0
        # for k in range(2,n):
        #     if(nums[i]>imax):
        #         imax = nums[i]
        #         jmin = nums[j]
        #     else:jmin = min(jmin,nums[j])
        #     max_diff = max(max_diff,imax-jmin)
        #     ans = max(ans,max_diff*nums[k])
        #     i+=1
        #     j+=1
        # return ans

        n = len(nums)
        prefix = [0]*n
        for j in range(1,n):
            prefix[j] = max(prefix[j-1],nums[j-1])
        
        suffix = [0]*n
        for j in range(n-2,0,-1):
            suffix[j] = max(suffix[j+1],nums[j+1])
        
        ans = 0
        for j in range(1,n-1):
            ans = max(ans,(prefix[j]-nums[j])*suffix[j])
        return ans

# time complexity: O(n),O(n)
# space complexity: O(1),O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))