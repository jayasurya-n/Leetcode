from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0]*26
        for ch in tasks:freq[ord(ch)-ord('A')]+=1
        
        maxHeap = [-f for f in freq if f>0]
        heapq.heapify(maxHeap)
        waitQueue = deque()
        
        time = 0
        while maxHeap or waitQueue:
            time+=1
            if(maxHeap):
                f = heapq.heappop(maxHeap)
                f+=1
                if f<0:waitQueue.append((f,time+n))
            
            if(waitQueue and waitQueue[0][1]==time):
                heapq.heappush(maxHeap,waitQueue.popleft()[0])
        
        return time
         
# time complexity: O(tlogt)
# space complexity: O(t)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))