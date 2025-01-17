from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        hash = set(dictionary)
        dp = [-1]*len(s)
        def solve(ind):
            if(ind>=len(s)):return 0
            if(dp[ind]!=-1):return dp[ind]
            
            ans = solve(ind+1)+1
            for i in range(ind,len(s)):
                if(s[ind:i+1] in hash):
                    ans = min(ans,solve(i+1))
            dp[ind] = ans
            return dp[ind]

        return solve(0)

# time complexity: O(n^2)
# space complexity: O(n+dict)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))