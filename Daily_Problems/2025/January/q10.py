from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        freq = defaultdict(int)
        for word in words2:
            hash = defaultdict(int)
            for ch in word:
                hash[ch]+=1
                freq[ch] = max(freq[ch],hash[ch])
        
        ans = []
        for word in words1:
            temp = defaultdict(int)
            for ch in word:temp[ch]+=1
            
            bool = True
            for ch,f in freq.items():
                if(f>temp[ch]):
                    bool = False
                    break
            if(bool):ans.append(word)
        return ans

# time complexity: O(m+n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))