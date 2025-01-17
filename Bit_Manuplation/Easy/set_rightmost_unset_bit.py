from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def setBit(self, n):
        temp = n
        i = 0
        while(temp!=0):
            if(temp&1==0):return n|(1<<i)
            temp>>=1
            i+=1
        return n|(1<<i)

# time complexity: O(logn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))