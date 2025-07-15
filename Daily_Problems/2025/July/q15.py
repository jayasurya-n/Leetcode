from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def isValid(self, word: str) -> bool:
        if(len(word)<3):return False
        
        vowels = cons = False
        for ch in word:
            if(ch.isalpha()):
                if(ch.lower() in "aeiou"):vowels=True
                else:cons=True
            elif(not ch.isdigit()):return False
        return vowels and cons

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))