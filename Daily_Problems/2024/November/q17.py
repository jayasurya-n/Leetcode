from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        pass


# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))