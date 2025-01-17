from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0
        while(l+1<n and arr[l]<=arr[l+1]):l+=1
        
        r = n-1
        while(r>0 and arr[r]>=arr[r-1]):r-=1
        
        if(l>=r):return 0
        
        ans = min(r,n-l-1)
        
        i,j = 0,r
        while(i<=l and j<n):
            if(arr[i]<=arr[j]):
                ans = min(ans,j-i-1)
                i+=1
            else:j+=1
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))