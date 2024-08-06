from typing import List,Optional
import sys
class Solution:
    # def findMaxChoclates(self,i,robot1,robot2,grid,dp):
    #     if(robot1<0 or robot1>=len(grid[0]) or 
    #         robot2<0 or robot2>=len(grid[0])):return -sys.maxsize

    #     if i == len(grid)-1:
    #         if robot1 == robot2:return grid[i][robot1]
    #         else:return grid[i][robot1] + grid[i][robot2]


    #     if(dp[i][robot1][robot2]!=-1):return dp[i][robot1][robot2]

    #     dp[i][robot1][robot2] = -sys.maxsize
    #     for j1 in range(-1,2):
    #         for j2 in range(-1,2):
    #             ans = 0
    #             if(robot1==robot2):ans = grid[i][robot1]
    #             else:ans = grid[i][robot1]+grid[i][robot2]
    #             dp[i][robot1][robot2] = max(dp[i][robot1][robot2],ans+self.findMaxChoclates(i+1,robot1+j1,robot2+j2,grid,dp))
    #     return dp[i][robot1][robot2]

    # def solve(self, n, m, grid):
    #     dp  = [[[-1 for j in range(m)] for _ in range(m)] for _ in range(n)]
    #     return self.findMaxChoclates(0,0,m-1,grid,dp)

    # def solve(self, n, m, grid):
    #     dp  = [[[0 for j in range(m)] for _ in range(m)] for _ in range(n)]

    #     for j1 in range(m):
    #         for j2 in range(m):
    #             if(j1==j2):dp[n-1][j1][j2] = grid[n-1][j1]
    #             else:dp[n-1][j1][j2] = grid[n-1][j1] + grid[n-1][j2]
        
    #     for i in range(n-2,-1,-1):
    #         for robot1 in range(m): 
    #             for robot2 in range(m):
    #                 dp[i][robot1][robot2] = -sys.maxsize
    #                 for j1 in range(-1,2):
    #                     for j2 in range(-1,2):
    #                         ans = 0
    #                         if(robot1==robot2):ans = grid[i][robot1]
    #                         else:ans = grid[i][robot1]+grid[i][robot2]
    #                         if(robot1+j1>=0 and robot1+j1<len(grid[0]) and 
    #                             robot2+j2>=0 and robot2+j2<len(grid[0])):
    #                             dp[i][robot1][robot2] = max(dp[i][robot1][robot2],ans+dp[i+1][robot1+j1][robot2+j2])
    #     return dp[0][0][m-1]

    def solve(self, n, m, grid):
        prev  = [[0 for j in range(m)] for _ in range(m)]

        for j1 in range(m):
            for j2 in range(m):
                if(j1==j2):prev[j1][j2] = grid[n-1][j1]
                else:prev[j1][j2] = grid[n-1][j1] + grid[n-1][j2]
        
        for i in range(n-2,-1,-1):
            curr  = [[-sys.maxsize for j in range(m)] for _ in range(m)]
            for robot1 in range(m): 
                for robot2 in range(m):
                    for j1 in range(-1,2):
                        for j2 in range(-1,2):
                            ans = 0
                            if(robot1==robot2):ans = grid[i][robot1]
                            else:ans = grid[i][robot1]+grid[i][robot2]
                            if(robot1+j1>=0 and robot1+j1<len(grid[0]) and 
                                robot2+j2>=0 and robot2+j2<len(grid[0])):
                                curr[robot1][robot2] = max(curr[robot1][robot2],ans+prev[robot1+j1][robot2+j2])
            prev = curr
        return prev[0][m-1]



# time complexity: O(n*m*m*9), O(n*m*m*9), O(n*m*m*9)
# space complexity: O(n*m*m+m*m(stack space)), O(n*m*m), O(m*m)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        n,m = list(map(int,input().strip().split()))
        grid = [list(map(int,input().strip().split())) for _ in range(n)]
        print(Solution().solve(n,m,grid))