from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = dict()
        ans = 0
        
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                predecessor = word[:i]+word[i+1:]
                if predecessor in dp:
                    dp[word] = max(dp[word],1+dp[predecessor])
            ans = max(ans,dp[word])
        return ans

# time complexity: O(nlogn*k+nk^2), k = average length of word
# space complexity: O(n*k)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))