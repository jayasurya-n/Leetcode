from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    # def minCut(self, s: str) -> int:
        # n = len(s)
        # dp = [[n+1]*n for _ in range(n)]
        # for i in range(n):dp[i][i] = 0
        
        # for l in range(2,n+1):
        #     for i in range(0,n-l+1):
        #         j = i+l-1
        #         if(s[i:j+1]==s[i:j+1][::-1]):dp[i][j] = 0
        #         else:
        #             for k in range(i,j):
        #                 dp[i][j] = min(dp[i][j],1+dp[i][k]+dp[k+1][j])
        # return dp[0][n-1]
    
    def minCut(self, s: str) -> int:
        n = len(s)
        isPalindrome = [[False]*n for _ in range(n)]
        for i in range(n):isPalindrome[i][i] = True
        
        for l in range(2,n+1):
            for i in range(0,n-l+1):
                j = i+l-1
                if(l==2):isPalindrome[i][j] = s[i]==s[j]
                else:isPalindrome[i][j] = (s[i]==s[j]) and isPalindrome[i+1][j-1]
        
        dp = [n+1]*n
        for i in range(n):
            if(isPalindrome[0][i]):dp[i] = 0
            else:
                for j in range(i):
                    if(isPalindrome[j+1][i]):
                        dp[i] = min(dp[i],dp[j]+1)
        
        return dp[n-1]
            
# time complexity: O(n^2)
# space complexity: O(n^2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))