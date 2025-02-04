from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans,csum = 0,nums[0]
        for i in range(len(nums)-1):
            if(nums[i]<nums[i+1]):csum+=nums[i+1]
            else:
                ans = max(ans,csum)
                csum = nums[i+1]
        return max(ans,csum)

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))