from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:    
    def minimumPlatform(self,arr,dep):
        events = []
        for i in range(len(arr)):
            events.append([arr[i],1])
            events.append([dep[i]+1,-1])
        
        events.sort()
        max_overlap = overlap = 0
        for _,type in events:
            overlap+=type
            max_overlap = max(max_overlap,overlap)
        return max_overlap

# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))