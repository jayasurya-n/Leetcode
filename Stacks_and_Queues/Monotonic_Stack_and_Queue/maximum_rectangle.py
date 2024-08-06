from typing import List,Optional
from collections import deque
import sys
class Solution:
    # def maximalRectangle(self, matrix: List[List[str]]):
    #     m,n = len(matrix),len(matrix[0])
        
    #     nseRow = [[0]*n for _ in range(m)]
    #     for i in range(m):
    #         stack =  []
    #         for j in range(n-1,-1,-1):
    #             while(stack and int(matrix[i][stack[-1]])>=int(matrix[i][j])):stack.pop()
    #             if(stack==[]):nseRow[i][j] = n
    #             else:nseRow[i][j] = stack[-1]
    #             stack.append(j)
        
    #     nseCol = [[0]*n for _ in range(m)]
    #     for j in range(n):
    #         stack =  []
    #         for i in range(m-1,-1,-1):
    #             while(stack and int(matrix[stack[-1]][j])>=int(matrix[i][j])):stack.pop()
    #             if(stack==[]):nseCol[i][j] = m
    #             else:nseCol[i][j] = stack[-1]
    #             stack.append(i)
        
    #     # print(nseRow)
    #     # print(nseCol)
        
    #     area = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if(matrix[i][j]=='1'):
    #                 index = nseRow[i][j]
    #                 ans = m
    #                 for k in range(j,index):
    #                     ans = min(nseCol[i][k]-i,ans)
    #                     area = max(area,ans*(k-j+1))
    #     return area

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
    
    def maximalRectangle(self, matrix: List[List[str]]):
        
        prefixSum = [[0]*n for _ in range(m)]
        for j in range(n):
            sum = 0
            for i in range(m):
                if(matrix[i][j]=='0'):sum=0
                else:sum+=1
                prefixSum[i][j]=sum
        
        ans = 0
        for i in range(m):
            ans = max(ans,self.largestRectangleArea(prefixSum[i]))
        return ans 
                
                        
                        
# time complexity: O(m*n*m),O(m*n)
# space complexity: O(m*n),O(m*n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))