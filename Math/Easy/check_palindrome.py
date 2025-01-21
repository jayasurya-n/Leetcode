from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):return False
        temp = x
        rev = 0
        while(temp!=0):
            digit = temp%10
            rev = rev*10+digit
            temp//=10
        return rev==x

# time complexity: O(logn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))