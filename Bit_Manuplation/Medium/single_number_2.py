from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            cnt = 0
            for num in nums:
                if(num&(1<<i)!=0):cnt+=1
            if(cnt%3==1):ans|=(1<<i)
        return ans if ans<(1<<31) else ans-(1<<32)

# time complexity: O(32n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))