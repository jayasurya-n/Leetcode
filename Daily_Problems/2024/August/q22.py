from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def findComplement(self, num: int):
        i,ans = 0,0
        while(num):
            digit = num & 1
            if(digit==0):ans+=1<<i
            num = num>>1
            i+=1
        return ans

        # bits = num.bit_length()
        # return num^((1<<bits)-1)
        
# time complexity: O(logn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        print(Solution().findComplement(n))