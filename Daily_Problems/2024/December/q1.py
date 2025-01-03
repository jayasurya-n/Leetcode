from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash = set(arr)
        for ele in arr:
            if(ele!=0 and 2*ele in arr):return True
        return True if sum([1 for ele in arr if ele==0])>1 else False

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))