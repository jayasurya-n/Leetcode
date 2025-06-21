from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = defaultdict(int)
        for ch in word:freq[ch]+=1

        ans = len(word)
        for f1 in freq.values():
            curr = 0
            for f2 in freq.values():
                if(f2<f1):curr+=f2
                elif(f2>f1+k):curr+=f2-(f1+k)
            ans = min(ans,curr)
        return ans

# time complexity: O(n+26^2)
# space complexity: O(26)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))