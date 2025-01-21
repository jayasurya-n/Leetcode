from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def sumOfDivisors(self, n):
        # ans = 0
        # for num in range(1,n+1):
        #     for i in range(1,int(num**0.5)+1):
        #         if(num%i==0):
        #             ans+=i
        #             if(i!=(num//i)):ans+=num//i
        # return ans

        ans = 0
        for i in range(1,n+1):
            ans+=(n//i)*i
        return ans
    
# time complexity: O(n^1.5),O(n)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))