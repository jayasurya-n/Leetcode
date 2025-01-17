from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        prefix = 1
        k-=1
        
        def countSteps(prefix):
            cur = prefix
            next = prefix+1
            steps = 0
            while(cur<=n):
                steps+=min(n+1,next)-cur
                cur*=10
                next*=10
            return steps
        
        while(k>0):
            steps = countSteps(prefix)
            if(steps<=k):
                prefix+=1
                k-=steps
            else:
                prefix*=10
                k-=1
        return prefix


# time complexity: O(logn^2)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))