from typing import List,Optional
import sys
class Solution:
    # def combination(self,n,r):
    #     ans = 1
    #     for i in range(1,r+1):
    #         ans*=n-i+1
    #         ans/=i
    #     return int(ans)
        
    # def uniquePaths(self, m: int, n: int) -> int:
    #     # m-1+n-1 C n-1
    #     if(m<n):
    #         return self.combination(m+n-2,m-1)
    #     return self.combination(m+n-2,n-1)

    # def findPaths(self,i,j,dp):
    #     if(i==0 and j==0):return 1
    #     elif(i<0 or j<0):return 0
    #     if(dp[i][j]!=-1):return dp[i][j]
    #     dp[i][j] = self.findPaths(i-1,j,dp)+self.findPaths(i,j-1,dp)
    #     return dp[i][j]

    # def uniquePaths(self, m: int, n: int) -> int:
    #     i,j = m-1,n-1 
    #     dp = [[-1]*n for _ in range(m)]
    #     ans =  self.findPaths(i,j,dp)
    #     print(dp)
    #     return ans

    # def uniquePaths(self, m: int, n: int) -> int:
    #     dp = [[-1]*n for _ in range(m)]
    #     for i in range(m):dp[i][0] = 1 
    #     for j in range(n):dp[0][j] = 1

    #     for i in range(1,m):
    #         for j in range(1,n):
    #             dp[i][j] = dp[i-1][j]+dp[i][j-1]
    #     return dp[m-1][n-1] 

    def uniquePaths(self, m: int, n: int) -> int:
            prevRow = [1]*n

            for i in range(1,m):
                prevColumn = 1
                for j in range(1,n):
                    ans = prevRow[j]+prevColumn
                    prevColumn = ans
                    prevRow[j] = ans
            return prevRow[n-1]



# time complexity: O(min(n,m)), O(m*n), O(m*n),O(m*n)
# space complexity: O(1), O(m*n+(m+n)(stack space)), O(m*n),O(n)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        m,n = list(map(int,input().strip().split()))
        print(Solution().uniquePaths(m,n))