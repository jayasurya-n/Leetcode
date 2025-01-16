from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        freq = defaultdict(int)
        for ch in s:freq[ch]+=1
        
        singles, doubles = 0,0
        for f in freq.values():
            singles+=f%2
            doubles+=f//2
            
        return True if singles<=k and 2*doubles>=k-singles else False

# time complexity: O(m)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))