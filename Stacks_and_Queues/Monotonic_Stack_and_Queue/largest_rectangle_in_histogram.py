from typing import List,Optional
from collections import deque
import sys
class Solution:
    # def largestRectangleArea(self, heights: List[int]):
    #     n = len(heights)
    #     nse = [0]*n
    #     stack = []
    #     for i in range(n-1,-1,-1):
    #         while(stack and heights[stack[-1]]>=heights[i]):stack.pop()
    #         if(stack==[]):nse[i] = n
    #         else:nse[i] = stack[-1]
    #         stack.append(i)
        
    #     pse = [0]*n
    #     stack = []
    #     for i in range(0,n):
    #         while(stack and heights[stack[-1]]>heights[i]):stack.pop()
    #         if(stack==[]):pse[i] = -1
    #         else:pse[i] = stack[-1]
    #         stack.append(i)
        
    #     ans = 0
    #     for i in range(n):
    #         ans = max(ans,(nse[i]-pse[i]-1)*heights[i])
    #     return ans
    
    def largestRectangleArea(self, heights: List[int]):
        n = len(heights)
        stack = []
        ans = 0
        for i in range(n):
            while(stack and heights[stack[-1]]>heights[i]):
                ele = heights[stack[-1]]
                stack.pop()
                nse = i
                if(stack==[]):pse = -1
                else:pse = stack[-1]
                ans = max(ans,(nse-pse-1)*ele)
            stack.append(i)
        
        while(stack):
            ele = heights[stack[-1]]
            nse = n
            stack.pop()
            if(stack==[]):pse = -1
            else:pse = stack[-1]
            ans = max(ans,(nse-pse-1)*ele)
        return ans

# time complexity: O(n), O(n)
# space complexity: O(n), O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        heights = list(map(int,input().strip().split()))
        print(Solution().largestRectangleArea(heights))