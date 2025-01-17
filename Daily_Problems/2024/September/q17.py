from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hash = dict()
        for word in s1.split():
            hash[word] = hash.get(word,0)+1
            
        for word in s2.split():
            hash[word] = hash.get(word,0)+1
        
        ans = []
        for word,val in hash.items():
            if(val==1):ans.append(word)
        return list(ans)
        
# time complexity: O(m+n)
# space complexity: O(m+n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))