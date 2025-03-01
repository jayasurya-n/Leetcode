from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # n1,n2 = len(str1),len(str2)
        # prev = [[] for _ in range(n2+1)]
        
        # for j in range(1,n2+1):
        #     prev[j] = prev[j-1]+[str2[j-1]]

        # for i in range(1,n1+1):
        #     curr = [[] for _ in range(n2+1)]
        #     curr[0] = list(str1[:i])
        #     for j in range(1,n2+1):
        #         if(str1[i-1]==str2[j-1]):
        #             curr[j] = prev[j-1]+[str1[i-1]]
        #         else:
        #             if(len(prev[j])<len(curr[j-1])):
        #                 curr[j] = prev[j]+[str1[i-1]]
        #             else:
        #                 curr[j] = curr[j-1]+[str2[j-1]]
            
        #     prev = curr
            
        # return "".join(curr[n2])


        n1,n2 = len(str1),len(str2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if(str1[i-1]==str2[j-1]):dp[i][j]=dp[i-1][j-1]+1
                else:dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        
        ans = []
        i,j = n1,n2
        while(i>0 and j>0):
            if(str1[i-1]==str2[j-1]):
                ans.append(str1[i-1])
                i-=1
                j-=1
            elif(dp[i][j]==dp[i-1][j]):
                    ans.append(str1[i-1])
                    i-=1
            else:
                ans.append(str2[j-1])
                j-=1
        
        while(i>0):
            ans.append(str1[i-1])
            i-=1
        
        while(j>0):
            ans.append(str2[j-1])
            j-=1
        return "".join(ans[::-1])
        
# time complexity: O(mn*(m+n)), O(mn)
# space complexity: O(n*(m+n)), O(mn)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))