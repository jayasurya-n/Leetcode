from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0 
        for bit in range(24):
            cnt = 0
            for num in candidates:
                if((num & (1<<bit))>0):cnt+=1
            ans = max(ans,cnt)
        return ans

# time complexity: O(n*24)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))