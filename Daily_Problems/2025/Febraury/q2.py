from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        i=0
        while(i<n-1 and nums[i]<=nums[i+1]):i+=1
        if(i==n-1):return True

        i+=1
        while(i<n-1):
            if(nums[i]<=nums[i+1] and nums[i]<=nums[0]):i+=1
            else:return False
        return nums[-1]<=nums[0]

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))