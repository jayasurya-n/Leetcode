from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def solve(self, bt):
        bt.sort()
        waiting = curr = 0
        for i in range(len(bt)):
            waiting+=curr
            curr+=bt[i]
        return waiting//len(bt)

# time complexity: O(nlogn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))