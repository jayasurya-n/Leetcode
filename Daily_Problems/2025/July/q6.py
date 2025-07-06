from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.hash = defaultdict(int)
        for num in nums2:self.hash[num]+=1

    def add(self, index: int, val: int) -> None:
        curr_val = self.nums2[index]
        self.hash[curr_val]-=1
        if(self.hash[curr_val]==0):self.hash.pop(curr_val)
        self.nums2[index]+=val
        self.hash[val+curr_val]+=1

    def count(self, tot: int) -> int:
        ans = 0
        for num in self.nums1:
            ans+=self.hash[tot-num]
        return ans

# time complexity: O(add: O(logn), count: nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(FindSumPairs().func(arr,n))