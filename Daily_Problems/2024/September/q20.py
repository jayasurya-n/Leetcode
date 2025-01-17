from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev_s = s[::-1]
        for i in range(len(s)):
            if(s[:len(s)-i]==rev_s[i:]):
                return rev_s[:i]+s
        return ""

# time complexity: O(n^2)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))