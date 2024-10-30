from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = [] #stores larger half of the numbers
        self.maxHeap = [] #stores smaller half of the numbers
        
    def addNum(self, num: int) -> None:
        if(not self.maxHeap or num<=-self.maxHeap[0]):heapq.heappush(self.maxHeap,-num)
        else:heapq.heappush(self.minHeap,num)
        
        if(len(self.minHeap)>len(self.maxHeap)):
            num = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap,-num)
        elif(len(self.maxHeap)>len(self.minHeap)+1):
            num = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,num)
            
            
    def findMedian(self) -> float:
        if(len(self.maxHeap)>len(self.minHeap)):return -self.maxHeap[0]
        else:return (self.minHeap[0]-self.maxHeap[0])/2


# time complexity: O(logn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))