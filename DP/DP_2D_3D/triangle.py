from typing import List,Optional
import sys
class Solution:
    # def findPathSum(self,i,j,dp,triangle):
    #     if(i==0 and j==0):return triangle[0][0]
    #     if(j<0 or j>=len(triangle[i])):return sys.maxsize

    #     if(dp[i][j]!=-1):return dp[i][j]
    #     dp[i][j] = triangle[i][j] + min(self.findPathSum(i-1,j,dp,triangle),self.findPathSum(i-1,j-1,dp,triangle))
    #     return dp[i][j]

    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     dp = []
    #     for i in range(len(triangle)):
    #         dp.append([-1]*len(triangle[i]))
        
    #     ans = sys.maxsize
    #     for j in range(len(triangle[-1])): 
    #         ans = min(ans,self.findPathSum(len(triangle)-1,j,dp,triangle))
    #     return ans
    
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     dp = []
    #     for i in range(len(triangle)):
    #         dp.append([-1]*len(triangle[i]))
        
    #     dp[0][0] = triangle[0][0]
    #     for i in range(1,len(triangle)):
    #         for j in range(len(triangle[i])):
    #             if(j==0):dp[i][j] = triangle[i][j] + dp[i-1][j]
    #             elif(j==len(triangle[i-1])):dp[i][j] = triangle[i][j] + dp[i-1][j-1]
    #             else:dp[i][j] = triangle[i][j] + min(dp[i-1][j],dp[i-1][j-1])
    #     return min(dp[-1])

    # def minimumTotal(self, triangle: List[List[int]]) -> int:
        
    #     prev = [triangle[0][0]]
    #     for i in range(1,len(triangle)):
    #         curr = [-1]*len(triangle[i])
    #         for j in range(len(triangle[i])):
    #             if(j==0):curr[j] = triangle[i][j] + prev[j]
    #             elif(j==len(triangle[i-1])):curr[j] = triangle[i][j] + prev[j-1]
    #             else:curr[j] = triangle[i][j] + min(prev[j],prev[j-1])
    #         prev = curr
    #     return min(prev)

    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                if(j==0):triangle[i][j] = triangle[i][j] + triangle[i-1][j]
                elif(j==len(triangle[i-1])):triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
                else:triangle[i][j] = triangle[i][j] + min(triangle[i-1][j],triangle[i-1][j-1])
        return min(triangle[-1])



# time complexity: O(n^2), O(n^2), O(n^2), O(n^2)
# space complexity: O(n^2+(n)(stack space)), O(n^2), O(n), O(1)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        m = int(input().strip())
        triangle = [list(map(int,input().strip().split())) for _ in range(m)]
        print(Solution().minimumTotal(triangle))