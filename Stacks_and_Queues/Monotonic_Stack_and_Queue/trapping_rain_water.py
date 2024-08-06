from typing import List,Optional
from collections import deque
import sys
class Solution:
    def trap(self, height: List[int]):
        n = len(height)
        
        leftMax = [0]*n
        maxi = -sys.maxsize
        for i in range(0,n):
            if(height[i]<=maxi):leftMax[i] = maxi
            else:
                leftMax[i] = -1
                maxi = height[i]
        
        rightMax = [0]*n
        maxi = -sys.maxsize
        for i in range(n-1,-1,-1):
            if(height[i]<=maxi):rightMax[i] = maxi
            else:
                rightMax[i] = -1
                maxi = height[i]
              
              
        ans = 0
        for i in range(n):
            if(leftMax[i]>height[i] and rightMax[i]>height[i]):
                ans+=min(leftMax[i],rightMax[i])-height[i]
        return ans


# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        height = list(map(int,input().strip().split()))
        print(Solution().trap(height))