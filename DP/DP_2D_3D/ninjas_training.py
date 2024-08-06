from typing import List,Optional
import sys
from sys import setrecursionlimit
setrecursionlimit(10**9)
class Solution:
    # def findMaximumPoints(self,day,lastTask,points,dp):
    #     if(day<0):return 0

    #     if(dp[day][lastTask]!=-1):return dp[day][lastTask]
    #     for i in range(0,3):
    #         if(i!=lastTask):
    #             dp[day][lastTask] = max(dp[day][lastTask],self.findMaximumPoints(day-1,i,points,dp)+points[day][i])
    #     return dp[day][lastTask]

    # def maximumPoints(self, points, n):
    #     dp = [[-1]*4 for _ in range(n)]
    #     day,lastTask = n-1,3
    #     ans = self.findMaximumPoints(day,lastTask,points,dp)
    #     print(dp)
    #     return ans

    # def maximumPoints(self, points, n):
    #     dp = [[-1]*3 for _ in range(n)]
    #     for i in range(3):dp[0][i] = points[0][i]

    #     for day in range(1,n):
    #         for task in range(0,3):
    #             for lastTask in range(0,3):
    #                 if(lastTask!=task):
    #                     dp[day][task] = max(dp[day][task],
    #                                        dp[day-1][lastTask]+points[day][task])
    #     return max(dp[n-1])
            

    def maximumPoints(self, points, n):
        prev = [-1]*3
        for i in range(3):prev[i] = points[0][i]

        for day in range(1,n):
            ans = [-1]*3
            for task in range(0,3):
                for lastTask in range(0,3):
                    if(lastTask!=task):
                        ans[task] = max(ans[task],points[day][task]+prev[lastTask])
            prev = ans 
        return max(prev)
            
            
# time complexity: O(4n*3(for loop)), O(n*3*3),O(n*3*3)
# space complexity: O(4n+n(stack space)), O(3*n),O(1)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        n = int(input().strip())
        points = [list(map(int,input().strip().split())) for _ in range(n)]
        print(Solution().maximumPoints(points,n))