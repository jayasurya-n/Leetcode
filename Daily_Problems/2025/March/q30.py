from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash = defaultdict(list)
        for i,ch in enumerate(s):hash[ch] = i
        
        ans = []
        curr_maxi = curr_length = 0
        for i,ch in enumerate(s):
            curr_maxi = max(curr_maxi,hash[ch])
            if(curr_maxi==i):
                new_length = curr_maxi+1-curr_length
                curr_length+=new_length
                ans.append(new_length)
                curr_maxi = i+1
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))