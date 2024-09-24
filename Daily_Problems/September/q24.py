from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        hash = set()
        for i in range(len(arr1)):
            num = arr1[i]
            while(num and num not in hash):
                hash.add(num)
                num//=10
        
        ans = 0
        for i in range(len(arr2)):
            num = arr2[i]
            while(num and num not in hash):num//=10
            if(num):
                ans = max(ans,len(str(num)))
        return ans
                
# time complexity: O(nlogn+mlogm)
# space complexity: O(nlogn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))