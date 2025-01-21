from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def print_divisors(self, n):
        ans1 = []
        ans2 = []
        for i in range(1,int(n**0.5)+1):
            if(n%i==0):ans1.append(i)
            multi = n//i
            if(n%multi==0 and multi!=i):ans2.append(multi)
        
        for i in range(len(ans1)):print(ans1[i],end=" ")
        for i in range(len(ans2)-1,-1,-1):print(ans2[i],end=" ")

# time complexity: O(n^0.5)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))