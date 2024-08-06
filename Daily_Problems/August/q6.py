from typing import List,Optional
from collections import deque
import sys
class Solution:
    def minimumPushes(self, word: str):
        arr = [0]*26
        for c in word:
            arr[ord(c)-97]+=1
        
        arr.sort(reverse=True)
        ans = 0
        for i in range(26):
            if(arr[i]==0):break
            ans+=arr[i]*(i//8+1)
        return ans
                
# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        word = input().strip()
        print(Solution().minimumPushes(word))