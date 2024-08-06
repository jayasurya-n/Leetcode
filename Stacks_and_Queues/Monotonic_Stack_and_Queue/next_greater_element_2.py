from typing import List,Optional
from collections import deque
import sys
class Solution:
    def nextGreaterElements(self, nums: List[int]):
        n = len(nums)
        nge = [0]*n
        stack = []
        
        for i in range(2*n-1,-1,-1):
            while(stack and nums[i%n]>=stack[-1]):stack.pop()
            if(i<n):
                if(stack==[]):nge[i] = -1
                else:nge[i] = stack[-1]
            stack.append(nums[i%n])
            
        return nge
            
            
# time complexity: O(4n)
# space complexity: O(2n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))