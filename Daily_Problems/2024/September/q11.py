from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # def getBinary(num):
        #     s=""
        #     for i in range(32):
        #         s = str(num%2)+s
        #         num//=2
        #     return s
        
        # s1 = getBinary(start)
        # s2 = getBinary(goal)
        # ans = 0
        # for i in range(32):
        #     if(s1[i]!=s2[i]):ans+=1
        # return ans

        xor = start^goal
        ans = 0
        while xor:
            ans+=xor & 1
            xor>>=1
        return ans
# time complexity: O(logn),O(logn)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))