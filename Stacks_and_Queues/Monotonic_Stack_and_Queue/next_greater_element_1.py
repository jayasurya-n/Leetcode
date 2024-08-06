from typing import List,Optional
from collections import deque
import sys
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]):
        nge = [0]*len(nums2)
        stack = []
        
        for i in range(len(nums2)-1,-1,-1):
            while(stack and stack[-1]<nums2[i]):stack.pop()
            if(stack==[]):nge[i] = -1
            else:nge[i] = stack[-1]
            stack.append(nums2[i])
        
        map = dict()
        for i in range(len(nums2)):
            map[nums2[i]] = i
        
        ans = []
        for i in range(len(nums1)):
            index = map[nums1[i]]
            ans.append(nge[index])
        return ans
        
# time complexity: O(2n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))