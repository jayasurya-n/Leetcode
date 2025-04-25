from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        hash = defaultdict(int)
        hash[0] = 1
        
        cnt = ans = 0
        for num in nums:
            if(num%modulo==k):cnt+=1
            ans+=hash[(cnt-k+modulo)%modulo]
            hash[cnt%modulo]+=1
        return ans
        
# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        nums = lii()
        modulo,k = lii()
        print(Solution().countInterestingSubarrays(nums,modulo,k))