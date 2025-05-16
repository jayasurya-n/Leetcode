from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [[0,-1]]*n
        
        # dp[i]: longest subsequence ending at index 'i'satisfying all conditions
        # transition: for j in range(i):if(check(i,j)):dp[i] = max(dp[i],1+dp[j])   
        # base: dp[i] = [1,-1]
        # final: max(dp)
        
        def check(i,j):
            if(len(words[i])!=len(words[j]) or 
               groups[i]==groups[j]):return False
            
            cnt = 0
            for k in range(len(words[i])):
                if(words[i][k]!=words[j][k]):cnt+=1
            return cnt==1            
        
        for i in range(n):dp[i] = [1,-1]
        
        for i in range(1,n):
            l = len(words[i])
            for j in range(i):
                if(check(i,j)):
                    if(dp[i][0]<1+dp[j][0]):
                        dp[i][0] = 1+dp[j][0]
                        dp[i][1] = j
        
        # for row in dp: print(row)
        maxi = -1
        end = None
        for i in range(n):
            if(maxi<dp[i][0]):
                maxi = dp[i][0]
                end = i

        ans = []        
        while(end!=-1):
            ans.append(words[end])
            end = dp[end][1]
        return ans[::-1]

# time complexity: O(n*n*L)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        words = lsi()
        groups = lii()
        print(Solution().getWordsInLongestSubsequence(words,groups))