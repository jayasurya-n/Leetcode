from typing import List,Optional
from collections import deque
import sys,heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.root = None
        self.k = k
        self.min_heap  = []
        for i in range(len(nums)):
            self.add(nums[i])

    def add(self, val: int):
        heapq.heappush(self.min_heap,val)
        if(len(self.min_heap)>self.k):
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


# time complexity: O(nlogn)
# space complexity: O(n)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)