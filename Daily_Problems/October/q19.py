from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def findK(n,k):
            if(n==1):return "0"
            len = (1<<n)-1
            mid = (len//2)+1
            
            if(k==mid):return "1"
            elif(k<mid):return findK(n-1,k)
            else:
                bit = findK(n-1,len-k+1)
                return "1" if bit=="0" else "0"
            
        return findK(n,k)

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))