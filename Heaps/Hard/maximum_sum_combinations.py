from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def solve(self, A, B, C):
        m,n = len(A),len(B)
        A.sort(reverse=True)
        B.sort(reverse = True)
    
        maxHeap = []
        visited = set()
        
        sum = A[0]+B[0]
        heapq.heappush(maxHeap,(-sum,0,0))
        visited.add((0,0))
        
        ans = []
        for _ in range(C):
            if(maxHeap):
                sum,i,j = heapq.heappop(maxHeap)
                ans.append(-sum)
            
                if(i+1<m and (i+1,j) not in visited):
                    heapq.heappush(maxHeap,(-A[i+1]-B[j],i+1,j))
                    visited.add((i+1,j))
                
                if(j+1<n and (i,j+1) not in visited):
                    heapq.heappush(maxHeap,(-A[i]-B[j+1],i,j+1))
                    visited.add((i,j+1))
        return ans
        
# time complexity: O(mlogm+nlogn+clogc)
# space complexity: O(c)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))