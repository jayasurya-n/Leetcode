from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # hash = defaultdict(int)
        # cnt = 0
        # for word in words:
        #     rev = word[::-1]
        #     if(hash[rev]!=0):
        #         hash[rev]-=1
        #         cnt+=1
        #     else:
        #         hash[word]+=1
        
        # for word in hash.keys():
        #     if(hash[word]!=0 and word==word[::-1]):
        #         return 4*cnt+2
        # return 4*cnt 

        hash = defaultdict(int)
        for word in words:
            hash[word]+=1   
        
        ans = 0
        bool = False
        for word in list(hash.keys()):
            if(word==word[::-1]):
                ans += 4*(hash[word]//2)
                if(hash[word]&1):bool = True
            elif(word<word[::-1]):
                ans += min(hash[word],hash[word[::-1]])*4
        return ans+2*bool

# time complexity: O(n),O(n)
# space complexity: O(n),O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))