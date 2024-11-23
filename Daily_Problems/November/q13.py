from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            low = bisect.bisect_left(nums,lower-nums[i],i+1,n)-(i+1)
            high = bisect.bisect_right(nums,upper-nums[i],i+1,n)-(i+1)
            ans+=high-low
        return ans

# time complexity: O(nlogn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))