from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ""
        for i in range(len(s)):
            num+=str(ord(s[i])-96)
        
        num = int(num)
        print(num)
        while(k):
            sum = 0
            while(num):
                sum+=num%10
                num//=10
            num = sum
            k-=1
        return num

# time complexity: O(k*logn+n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s = input().strip()
        k = int(input().strip())
        print(Solution().getLucky(s,k))