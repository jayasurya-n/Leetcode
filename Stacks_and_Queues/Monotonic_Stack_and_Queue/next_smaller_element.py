from typing import List,Optional
from collections import deque
import sys
class Solution:
    def prevSmaller(self, nums):
        nse = []
        stack = []
        for i in range(len(nums)):
            while(stack and stack[-1]>=nums[i]):stack.pop()
            if(stack==[]):nse.append(-1)
            else:nse.append(stack[-1])
            stack.append(nums[i])
        return nse
            
# time complexity: O(2n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))


