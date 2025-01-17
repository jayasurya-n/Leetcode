from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def strangePrinter(self, s: str):
        ns = s[0]
        i = 1
        while(i<len(s)):
            while(i<len(s) and s[i]==s[i-1]):i+=1
            if(i<len(s)):ns+=s[i]
            i+=1
        
        s=ns
        n = len(s)
        def solve(start,end):
            if(start>end):return 0
            
            if(dp[start][end]!=-1):return dp[start][end]
            
            ans = 1+solve(start+1,end)
            for i in range(start+1,end+1):
                if(s[i]==s[start]):
                    ans = min(ans,solve(start,i-1)+solve(i+1,end))
            
            dp[start][end] = ans
            return ans

        dp = [[-1]*n for _ in range(n)]
        return solve(0,n-1)


# time complexity: O(n^3)
# space complexity: O(n^2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s = input().strip()
        print(Solution().strangePrinter(s))