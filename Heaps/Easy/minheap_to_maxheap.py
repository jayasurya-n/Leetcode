from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq
    
class Solution:
    def convertMinToMaxHeap(self, n, arr):
        def heapifyDown(i):
            if(i>=n):return 
            largest = i
            l = 2*i+1
            r = 2*i+2
            
            if(l<n and arr[l]>arr[largest]):largest = l
            if(r<n and arr[r]>arr[largest]):largest = r
            
            if(largest!=i):
                arr[i],arr[largest] = arr[largest],arr[i]
                heapifyDown(largest)
        
        for i in range((n//2)-1,-1,-1):heapifyDown(i)
             
# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().convertMinToMaxHeap(n,arr))