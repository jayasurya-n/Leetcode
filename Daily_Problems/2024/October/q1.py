from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        hash = dict()
        for i in range(len(arr)):
            r1 = arr[i]%k
            r2 = (k-r1)%k
            if(r2 in hash):
                hash[r2]-=1
                if(hash[r2]==0):hash.pop(r2)
            else:hash[r1] = hash.get(r1,0)+1
            print(hash)
        
        return len(hash)==0

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = list(map(int,input().strip().split()))
        k = int(input().strip())
        print(Solution().canArrange(arr,k))