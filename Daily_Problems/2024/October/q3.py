from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        hash = {0:-1}
        tsum = sum(nums)
        csum = 0
        
        if(tsum%p==0):return 0
        ans = sys.maxsize
        for i in range(len(nums)):
            csum+=nums[i]
            eq = (csum%p - tsum%p + p)%p
            if(eq in hash):
                ans = min(ans,i-hash[eq])
            hash[csum%p]=i
        
        return ans if(ans!=len(nums)) else -1
                
# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        nums = list(map(int,input().strip().split()))
        p = int(input().strip())
        print(Solution().minSubarray(nums,p))