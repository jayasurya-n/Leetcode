from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        while(len(self.minHeap)>self.k):heapq.heappop(self.minHeap)
        return self.minHeap[0]

# time complexity: O(logk) for each operation
# space complexity: O(k)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))