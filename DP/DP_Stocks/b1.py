from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low,high = 0,len(arr)-1
        while(low<=high):
            mid = (low+high)//2
            missing = arr[mid]-(mid+1)
            if(missing>=target):high = mid-1
            else:low=mid+1
        return low+k
                
# time complexity: O(logn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))