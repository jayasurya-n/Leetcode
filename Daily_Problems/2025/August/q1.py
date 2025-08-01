from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for _ in range(2,numRows+1):
            prev = ans[-1]
            curr = [1]
            for i in range(len(prev)-1):
                curr.append(prev[i]+prev[i+1])
            curr.append(1)
            ans.append(curr)
        return ans

# time complexity: O(n^2)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))