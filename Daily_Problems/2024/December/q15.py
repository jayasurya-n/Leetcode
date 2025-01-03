from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        maxheap = [(-(t-p)/(t*(t+1)),i) for i,(p,t) in enumerate(classes) if p!=t]
        heapq.heapify(maxheap) 
        if(not maxheap):return 1
        
        for _ in range(extraStudents):
            _,i = heapq.heappop(maxheap)
            classes[i][0]+=1
            classes[i][1]+=1
            p,t = classes[i]
            heapq.heappush(maxheap,(-(t-p)/(t*(t+1)),i))

        ans = 0
        for p,t in classes:ans+=p/t
        return ans/len(classes) 

# time complexity: O(n+mlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))