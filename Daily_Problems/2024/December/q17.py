from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = [0]*26
        for ch in s:freq[ord(ch)-97]+=1
        
        ans = []
        for i in range(25,-1,-1):
            j = i-1
            while(freq[i]>0):
                f = min(freq[i],repeatLimit)
                ans.append(f*chr(i+97))
                freq[i]-=f
                while(j>=0 and freq[j]==0):j-=1
                if(freq[i]==0 or j<0):break
                else:
                    ans.append(chr(j+97))
                    freq[j]-=1
        
        return "".join(ans)

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s = input().strip()
        repeatLimit = int(input().strip())
        print(Solution().repeatLimitedString(s,repeatLimit))