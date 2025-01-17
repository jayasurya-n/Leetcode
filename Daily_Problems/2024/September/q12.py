from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = len(words)
        st = set()
        for ch in allowed:st.add(ch)
        
        for word in words:
            for ch in word:
                if(ch not in st):
                    ans-=1
                    break
        return ans

# time complexity: O(n+m)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))