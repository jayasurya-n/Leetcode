from typing import List,Optional
import sys
class Solution:

    def backtrack(self,i,j,text1,text2,dp):
        if(i==0 or j==0):
            return {""}
        
        if(text1[i-1]==text2[j-1]):
            res = set()
            ans = self.backtrack(i-1,j-1,text1,text2,dp)
            for string in ans:
                res.add(string+text1[i-1])
            return res
        
        else:
            ans = set()
            if(dp[i-1][j]>=dp[i][j-1]):
                ans.update(self.backtrack(i-1,j,text1,text2,dp))
            if(dp[i][j-1]>=dp[i-1][j]):
                ans.update(self.backtrack(i,j-1,text1,text2,dp))
            return ans


    def all_longest_common_subsequences(self, text1, text2):
        l1 = len(text1)
        l2 = len(text2)
        dp = [[0]*(l2+1) for _ in range(l1+1)]
        
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if(text1[i-1]==text2[j-1]):
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        ans = self.backtrack(l1,l2,text1,text2,dp)
        return sorted(list(ans))



# time complexity: O(l1*l2)
# space complexity: O(l1*l2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        text1 = input().strip()
        text2 = input().strip()
        print(Solution().all_longest_common_subsequences(text1,text2))