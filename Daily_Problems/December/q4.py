from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0
        for ch in str1:
            nch = ''
            if(ch=='z'):nch='a'
            else:nch = chr(ord(ch)+1)
            if(j<len(str2) and (ch==str2[j] or nch==str2[j])):j+=1
        return j==len(str2)

# time complexity: O(m+n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))