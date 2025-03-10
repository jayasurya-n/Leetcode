from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # vowels = ['a','e','i','o','u']
        # constants = 0
        # hash = defaultdict(int)
        
        # n = len(word)
        # next_constanst = [-1]*n
        # next = n
        # for i in range(n-1,-1,-1):
        #     next_constanst[i] = next
        #     if(word[i] not in vowels):next = i
        
        # ans = 0
        # i = j = 0
        # while(j<n):
        #     if(word[j] in vowels):hash[word[j]]+=1
        #     else:constants+=1
            
        #     while(i<j and constants>k):
        #         if(word[i] in vowels):
        #             hash[word[i]]-=1
        #             if(hash[word[i]]==0):hash.pop(word[i])
        #         else:constants-=1
        #         i+=1
            
        #     while(i<j and len(hash)==5 and constants==k):
        #         ans+=next_constanst[j]-j
        #         if(word[i] in vowels):
        #             hash[word[i]]-=1
        #             if(hash[word[i]]==0):hash.pop(word[i])
        #         else:constants-=1
        #         i+=1
            
        #     j+=1

        # return ans
        
        def countatleastK(k):
            vowels = ['a','e','i','o','u']
            constants = 0
            hash = defaultdict(int)
            
            n = len(word)
            ans = 0
            i = j = 0
            while(j<n):
                if(word[j] in vowels):hash[word[j]]+=1
                else:constants+=1
                
                while(i<j and len(hash)==5 and constants>=k):
                    ans+=n-j
                    if(word[i] in vowels):
                        hash[word[i]]-=1
                        if(hash[word[i]]==0):hash.pop(word[i])
                    else:constants-=1
                    i+=1
                
                j+=1
            
            return ans

        return countatleastK(k)-countatleastK(k+1)

# time complexity: O(n),O(n)
# space complexity: O(n),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))