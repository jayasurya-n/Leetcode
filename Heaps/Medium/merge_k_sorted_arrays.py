from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def mergeKArrays(self, arr, k):
        ans = []
        pq = []
        for i in range(k):heapq.heappush(pq,(arr[i][0],i,0))
        
        while pq:
            mini,i,j = heapq.heappop(pq)
            ans.append(mini)
            if(j+1<len(arr[i])):
                heapq.heappush(pq,(arr[i][j+1],i,j+1))
        return ans  

# time complexity: O(k^2logk)
# space complexity: O(k)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))