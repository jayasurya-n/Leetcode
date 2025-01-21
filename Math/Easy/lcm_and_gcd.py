from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        def find_gcd(a,b):
            while(b!=0):a,b = b,a%b
            return a
        gcd = find_gcd(a,b)
        return [a*b//gcd,gcd]

# time complexity: O(log(min(a,b)))
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))