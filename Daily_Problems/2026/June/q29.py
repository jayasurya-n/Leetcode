from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        n = len(word)

        def find_lps(pattern):
            m = len(pattern)
            lps = [0]*m
            length = 0
            i = 1

            while i<m:
                if(pattern[i]==pattern[length]):
                    length+=1
                    lps[i] = length
                    i+=1
                else:
                    if(length==0):
                        lps[i] = 0
                        i+=1
                    else:
                        length = lps[length-1]
            return lps
        
        ans = 0
        for pattern in patterns:
            lps = find_lps(pattern)
            m = len(pattern)

            i = j = cnt = 0
            while i<n:
                if(word[i]==pattern[j]):
                    i+=1
                    j+=1

                    if(j==m):
                        cnt+=1
                        j = lps[j-1]
                
                else:
                    if(j==0):
                        i+=1
                    else: 
                        j = lps[j-1]
            
            ans+=(cnt>0)
        return ans

# time complexity: O(n*k + sum(m))
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))