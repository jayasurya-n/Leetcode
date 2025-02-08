from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class NumberContainers:
    def __init__(self):
        self.index_to_number = defaultdict(int)
        self.number_to_indices = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.index_to_number[index] = number
        pq = self.number_to_indices[number]
        heapq.heappush(pq,index)
        

    def find(self, number: int) -> int:
        pq = self.number_to_indices[number]
        if not pq: return -1
        
        while pq:
            index = pq[0]
            if self.index_to_number[index]==number:return index
            heapq.heappop(pq)
        return -1

# time complexity: O(logn,klogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))