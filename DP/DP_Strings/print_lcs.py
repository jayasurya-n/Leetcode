from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def all_longest_common_subsequences(self, text1, text2):
        n1,n2 = len(text1),len(text2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if(text1[i-1]==text2[j-1]):dp[i][j]=dp[i-1][j-1]+1
                else:dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        
        # def backtrack(i,j,temp,ans):
        #     if i==0 or j==0:
        #         ans.add("".join(reversed(temp)))
        #         return
            
        #     if(text1[i-1]==text2[j-1]):
        #         temp.append(text1[i-1])
        #         backtrack(i-1,j-1,temp,ans)
        #         temp.pop()
            
        #     else:
        #         if(dp[i][j]==dp[i-1][j]):backtrack(i-1,j,temp,ans)
        #         if(dp[i][j]==dp[i][j-1]):backtrack(i,j-1,temp,ans)
        
        # ans = set()
        # backtrack(n1,n2,[],ans)
        # return sorted(ans)
        
        def backtrack(i,j,memo):
            if i==0 or j==0:return {""}
            
            if (i,j) in memo:return memo[(i, j)]
        
            lcs_set = set()
            if text1[i-1] == text2[j - 1]:
                temp = backtrack(i-1, j-1,memo)
                for seq in temp:
                    lcs_set.add(seq + text1[i - 1])
            else:
                if dp[i-1][j]>=dp[i][j-1]:lcs_set.update(backtrack(i-1,j,memo))
                if dp[i][j-1]>=dp[i-1][j]:lcs_set.update(backtrack(i,j-1,memo))
        
            memo[(i,j)] = lcs_set
            return lcs_set
        
        memo = dict()
        ans = backtrack(n1,n2,memo)
        return sorted(ans)

# time complexity: O(mn+k*L),k=unique lcs strings of length L
# space complexity: O(mn+k*L)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        text1 = input().strip()
        text2 = input().strip()
        print(Solution().all_longest_common_subsequences(text1,text2))