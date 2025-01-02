from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = {'a','e','i','o','u'}
        psum = [0]*n
        for i,word in enumerate(words):
            psum[i] = psum[i-1] if i>0 else 0
            if(word[0] in vowels and word[-1] in vowels):psum[i]+=1
        
        ans = []
        for l,r in queries:
            ans.append(psum[r]-(psum[l-1] if l>0 else 0))
        return ans

# time complexity: O(m+n)
# space complexity: O(m)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))