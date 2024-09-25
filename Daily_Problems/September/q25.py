from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        hash = dict()
        for word in words:
            for i in range(1,len(word)+1):
                hash[word[:i]] = hash.get(word[:i],0)+1
        
        ans = []
        for word in words:
            cnt = 0
            for i in range(1,len(word)+1):
                cnt+=hash.get(word[:i],0)
            ans.append(cnt)
        return ans

# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))