from typing import List,Optional
import sys
class Solution:
    def findPathSum(self,i,j,dp,matrix):
        if(j<0 or j>=len(matrix)):return sys.maxsize
        if(i==0):return matrix[i][j]

        if(dp[i][j]!=-1):return dp[i][j]
        dp[i][j] = matrix[i][j] + min(self.findPathSum(i-1,j-1,dp,matrix),self.findPathSum(i-1,j,dp,matrix),self.findPathSum(i-1,j+1,dp,matrix))
        return dp[i][j]

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[-1]*n for _ in range(n)]
        
        ans = sys.maxsize
        for j in range(n): 
            ans = min(ans,self.findPathSum(n-1,j,dp,matrix))
        return ans
    

    # def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    #     n = len(matrix)
    #     for i in range(1,n):
    #         for j in range(n):
    #             print("i,j",i,j)
    #             if(j==0):matrix[i][j] = matrix[i][j] + min(matrix[i-1][j],matrix[i-1][j+1])
    #             elif(j==n-1):matrix[i][j] = matrix[i][j] + min(matrix[i-1][j],matrix[i-1][j-1])
    #             else:matrix[i][j] = matrix[i][j] + min(matrix[i-1][j-1],matrix[i-1][j],matrix[i-1][j+1])
    #     return min(matrix[-1])



# time complexity: O(n^2), O(n^2)
# space complexity: O(n^2+n(stack space)), O(1)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        n = int(input().strip())
        matrix = [list(map(int,input().strip().split())) for _ in range(n)]
        print(Solution().minFallingPathSum(matrix))