from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # n = len(word)
        # k = numFriends
        # if(k==1):return word

        # # i+n-1-e>=k-1
        # # => e<=i+n-k
        # ans = ""
        # for i in range(n):
        #     end = min(n-1,i+n-k)
        #     candidate = word[i:end+1]
        #     if(candidate>ans):
        #         ans = candidate
        # return ans

        n = len(word)
        if(numFriends==1):return word

        i,j = 0,1
        while j<n:
            k = 0
            while j+k<n and word[i+k]==word[j+k]:k+=1
            if(j+k<n and word[i+k]<word[j+k]):
                i,j = j,max(j+1,i+k+1)
            else:j = j+k+1
        
        largest_lexo_suffix = word[i:]
        m = len(largest_lexo_suffix)
        return largest_lexo_suffix[:min(m,n-numFriends+1)]

# time complexity: O(n^2),O(n)
# space complexity: O(n),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))