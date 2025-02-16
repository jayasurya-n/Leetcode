from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        def rec(ind,hash,arr):
            if(ind==2*n-1):
                nonlocal ans
                ans = arr[:]
                return True
            
            if(arr[ind]!=-1):return rec(ind+1,hash,arr)
            
            for num in range(n,0,-1):
                if(num in hash):continue
                if(num==1 or (ind+num<2*n-1 and arr[ind+num]==-1)):
                    arr[ind] = num
                    if(num!=1):arr[ind+num] = num
                    hash.add(num)
                    if(rec(ind+1,hash,arr)):return True
                    arr[ind] = -1
                    if(num!=1):arr[ind+num] = -1
                    hash.remove(num)
            return False
        
        ans = None
        arr = [-1]*(2*n-1)
        hash = set()
        rec(0,hash,arr)
        return ans
                        
# time complexity: O(n!)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        print(Solution().constructDistancedSequence(n))