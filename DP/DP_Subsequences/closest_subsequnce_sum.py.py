from typing import List,Optional
import sys
class Solution:
    def minAbsDifference(self, nums: List[int], target: int) -> int:
        n = len(nums)
        goal = abs(target)
        dp = [[False]*(2*goal+1) for _ in range(n)]

        for i in range(n):
            dp[i][goal] = True
        
        if(0<=nums[i]+goal<=2*goal):dp[0][nums[i]+goal] = True

        for i in range(1,n):
            for s in range(0,2*goal+1):
                dp[i][s] = dp[i-1][s]
                if(0<=s-(nums[i]+goal)<=2*goal):
                    dp[i][s] = dp[i][s] or dp[i-1][s-nums[i]-goal]
        
        for row in dp:print(row)
        ans = sys.maxsize
        for j in range(0,2*goal+1):
            if(dp[n-1][j]==True):
                ans = min(ans,abs((dp[n-1][j]-goal)-target))
        return ans
        




# time complexity: O(n*goal)
# space complexity: O(n*goal)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        nums = list(map(int,input().strip().split()))
        goal = int(input().strip())
        print(Solution().minAbsDifference(nums,goal))