from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        curr = ""
        cnt = 1
        for ch in sentence:
            if(ch==" "):
                if(curr.startswith(searchWord)):return cnt
                curr = ""
                cnt+=1
            else:curr+=ch
        return cnt if curr.startswith(searchWord) else -1

# time complexity: O(n+wm)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))