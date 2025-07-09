from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [startTime[0]]
        for i in range(n-1):
            gaps.append(startTime[i+1]-endTime[i])
        gaps.append(eventTime-endTime[n-1])

        ans = csum = sum(gaps[:k+1])
        print(ans)
        for i in range(k+1,n+1):
            csum+=gaps[i]-gaps[i-k-1]
            ans = max(ans,csum)
        return ans

# time complexity: O(n+k)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))