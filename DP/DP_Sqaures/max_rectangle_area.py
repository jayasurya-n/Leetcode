from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix),len(matrix[0])
        ans = 0
    
        def largestRectangleArea(heights):
            heights = [0]+heights+[0]
            ans = 0
            stack = []
            for i in range(len(heights)):
                while(stack and heights[stack[-1]]>=heights[i]):
                    h = heights[stack.pop()]
                    w = i-stack[-1]-1 if stack else i
                    ans = max(ans,h*w)
                stack.append(i)
            return ans 
        
        heights = [0]*n
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]=="1"):heights[j]+=1
                else:heights[j] = 0
            ans = max(ans,largestRectangleArea(heights))
        return ans
                
# time complexity: O(mn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))