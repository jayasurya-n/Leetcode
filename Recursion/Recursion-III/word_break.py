from typing import List,Optional
import sys
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False]*len(s)

        for i in range(len(s)):
            for word in wordDict:
                if i<len(word)-1:continue

                if(i==len(word)-1 or dp[i-len(word)]):
                    if(s[i-len(word)+1:i+1]==word):
                        dp[i] = True
        return dp[len(s)-1]
    

# time complexity: O(s*dict*k), k is average length of word in dict
# space complexity: O(s)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))