from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        masking = [0]*26
        masking[ord('a')-97] = 1
        masking[ord('e')-97] = 2
        masking[ord('i')-97] = 4
        masking[ord('o')-97] = 8
        masking[ord('u')-97] = 16

        pxor = 0
        hash = dict()
        hash[0] = -1
        ans = 0
        for i in range(len(s)):
            pxor^=masking[ord(s[i])-97]
            if(pxor in hash):
                ans = max(ans,i-hash[pxor])
            else:hash[pxor] = i
        return ans
                
# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s = input().strip()
        print(Solution().findTheLongestSubstring(s))