from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        cnt = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                lsub = words[i]
                # if(words[j][:lsub]==words[i] and words[j][-lsub:]==words[i]):cnt+=1
                if(words[j].startswith(words[i]) and words[j].endswith(words[i])):cnt+=1
        return cnt

# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))