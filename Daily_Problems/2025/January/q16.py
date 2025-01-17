from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        if(len(nums2)%2==1):
            for num in nums1:ans^=num
        if(len(nums1)%2==1):
            for num in nums2:ans^=num
        return ans

# time complexity: O(m+n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))