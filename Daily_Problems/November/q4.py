from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        ans = []
        i = 0
        while i<n:
            cnt = 0
            ch = word[i]
            while(i<n and cnt<9 and word[i]==ch):
                cnt+=1
                i+=1
            ans.append(str(cnt))
            ans.append(ch)
        return "".join(ans)
    
# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))