from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def isPrime(self,n:int):
        if(n<=1):return False
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):return False
        return true

# time complexity: O(n*0.5)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))