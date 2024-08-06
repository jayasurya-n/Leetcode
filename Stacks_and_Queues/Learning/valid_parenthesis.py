from typing import List,Optional
from collections import deque
import sys
class Solution:
    def isValid(self, s: str):
        stack = []
        for c in s:
            if c in '([{':stack.append(c)
            else:
                if (stack==[] or 
                (c==')' and stack[-1]!='(') or
                (c==']' and stack[-1]!='[') or
                (c=='}' and stack[-1]!='{')):return False
                
                stack.pop()
                
        return stack==[]

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s = input().strip()
        print(Solution().isValid(s))