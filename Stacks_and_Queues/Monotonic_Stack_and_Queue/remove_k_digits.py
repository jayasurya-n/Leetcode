from typing import List,Optional
from collections import deque
import sys
class Solution:
    def removeKdigits(self, num: str, k: int):
        stack = []
        for i in range(len(num)):
            while(stack and k and int(stack[-1])>int(num[i])):
                stack.pop()
                k-=1
            stack.append(num[i])
        
        
        for i in range(k):stack.pop()
        if(k==len(num)):return '0'
        ans = ''
        start = True
        for c in stack:
            if(c=='0' and start):continue
            ans+=c
            start = False
        if(ans==''):return '0'
        return ans
            

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        num = input().strip()
        k = int(input().strip())
        print(Solution().removeKdigits(num,k))