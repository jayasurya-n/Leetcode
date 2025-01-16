from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def minimumLength(self, s: str) -> int:
        freq = defaultdict(int)
        for ch in s:freq[ch]+=1
        
        ans = 0
        for ch in freq:
            ans+=2 if freq[ch]%2==0 else 1
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))