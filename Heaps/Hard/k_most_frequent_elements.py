from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(int)
        for ele in nums:hash[ele]+=1
        
        minHeap = []
        for val,f in hash.items():
            heapq.heappush(minHeap,(f,val))
            if(len(minHeap)>k):heapq.heappop(minHeap)
        return [x[1] for x in minHeap]  
        
        # klogk+(n-k)logk=nlogk
# time complexity: O(nlogk)
# space complexity: O(n+k)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))