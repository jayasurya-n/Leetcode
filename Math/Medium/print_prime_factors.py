from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def AllPrimeFactors(self, n):
        ans = []
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                ans.append(i)
                while(n%i==0):n//=i
        
        if n!=1:ans.append(n)
        return ans

# time complexity: O(n^0.5logn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))