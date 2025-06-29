from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        hash = defaultdict(int)
        for ch in s:hash[ch]+=1

        candidates = [ch for ch in hash.keys() if hash[ch]>=k]
        candidates.sort(reverse=True)

        def is_subsequnce(s,sub):
            target=sub*k
            i = 0
            for ch in s:
                if(ch==target[i]):i+=1
                if(i>=len(target)):break
            return i==len(target)

        def backtrack(sub):
            if(len(sub)>0 and not is_subsequnce(s,sub)):return
            if(len(self.ans)<len(sub) or 
               (len(self.ans)==len(sub) and self.ans<sub)):
                    self.ans = sub
                
            for ch in candidates:
                backtrack(sub+ch)

        self.ans = ''
        backtrack('')
        return self.ans

# time complexity: O(n*(26)^L)
# space complexity: O(L)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))