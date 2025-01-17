from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        pxor = [0]*n
        pxor[0] = arr[0]
        for i in range(1,n):
            pxor[i] = pxor[i-1]^arr[i]
        
        ans = []
        for i,j in queries:
            s = pxor[j]
            if(i>0):s^=pxor[i-1]
            ans.append(s)
        return ans            

# time complexity: O(n+q)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))