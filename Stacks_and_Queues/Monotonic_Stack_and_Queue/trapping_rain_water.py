from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def trap(self, height: List[int]) -> int:
        # this solution is based on the idea that whnever there is a larger tower than the 
        # top of the stack i means there is potenial to trap water and we count the trapped water 
        # while poopping elmenets from the stack and computing width of the trapped water. 
        stack = []
        ans = 0
        for i in range(len(height)):
            while(stack and height[stack[-1]]<height[i]):
                curr = stack.pop()
                if(not stack):break
                
                width = i-stack[-1]-1
                ans+=(min(height[stack[-1]],height[i])-height[curr])*(width)
            stack.append(i)
        return ans

    # def trap(self, height: List[int]) -> int:
    #     n = len(height)
    #     rm = [0]*n
    #     rm[n-1] = height[n-1]
    #     for i in range(n-2,-1,-1):
    #         rm[i] = max(rm[i+1],height[i])
            
    #     lm = [0]*n
    #     lm[0] = height[0]
    #     for i in range(1,n):
    #         lm[i] = max(lm[i-1],height[i])
        
    #     ans = 0
    #     for i in range(n):
    #         ans+=(min(lm[i],rm[i])-height[i])
    #     return ans

# time complexity: O(n),O(n)
# space complexity: O(n),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))