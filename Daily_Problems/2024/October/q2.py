from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = arr.copy()
        arr.sort()
        rank = 0
        hash = dict()
        for i in range(len(arr)):
            if(arr[i] in hash):continue
            rank+=1
            hash[arr[i]]= rank
            
        ans = []
        for i in range(len(temp)):
            ans.append(hash[temp[i]])
        return ans

# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))