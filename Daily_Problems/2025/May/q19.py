from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # a,b,c = nums
        # if(a+b<=c or b+c<=a or c+a<=b):return "none"

        # if(a==b and b==c):return "equilateral"
        # elif(a==b or b==c or c==a):return "isosceles"
        # return "scalene"

        a,b,c = sorted(nums)
        if(a+b<=c):return "none"
        if(a==c):return "equilateral"
        elif(a==b or b==c):return "isosceles"
        return "scalene"

# time complexity: O(1),O(1)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))