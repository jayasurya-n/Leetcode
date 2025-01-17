from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def sumPrefixScores(self, words: List[str]):
        hash = dict()
        for word in words:
            prefix = ""
            for ch in word:
                prefix+=ch
                hash[prefix] = hash.get(prefix,0)+1
        
        ans = []
        for word in words:
            cnt = 0
            prefix = ""
            for ch in word:
                prefix+=ch
                cnt+=hash.get(prefix,0)
            ans.append(cnt)
        return ans

# time complexity: O(nl)
# space complexity: O(nl)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))