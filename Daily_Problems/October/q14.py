from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for ele in nums:heapq.heappush(maxHeap,-ele)
        
        score = 0
        for _ in range(k):
            maxi = -heapq.heappop(maxHeap)
            score+=maxi
            temp = (maxi+2)//3
            heapq.heappush(maxHeap,-temp)
        return score
            
# time complexity: O(nlogn+klogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))