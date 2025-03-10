from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect
from functools import cmp_to_key

class Solution:
    def fractionalknapsack(self, values, weights, capacity):
        items = sorted(zip(weights,values),key=lambda x:x[1]/x[0],reverse=True)
        ans = 0
        for i in range(len(items)):
            w,val = items[i]
            if(capacity<=w):
                ans+=(capacity/w)*val
                break
            ans+=val
            capacity-=w
        return ans    

# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))