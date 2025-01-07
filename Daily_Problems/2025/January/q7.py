from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if(i!=j):
                    if(words[i] in words[j]):
                        ans.append(words[i])
                        break
        return ans

# time complexity: O(m*n^2)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))