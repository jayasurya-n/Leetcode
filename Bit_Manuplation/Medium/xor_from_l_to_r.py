from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def findXOR(self, l, r):
        # xor of numbers from 1 to n has a pattern
        # if n=4k, xor = n
        # if n=4k+1, xor = 1
        # if n=4k+2, xor = n+1
        # if n=4k+3, xor = 0
        def find_xor(n):
            if(n%4==0):return n
            if(n%4==1):return 1
            if(n%4==2):return n+1
            if(n%4==3):return 0
        
        return find_xor(r)^find_xor(l-1)

# time complexity: O(1)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))