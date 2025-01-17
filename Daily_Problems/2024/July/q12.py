from typing import List,Optional
import sys
class Solution:

    def findMaxGain(self,s,x,y,ch1,ch2):
        # x,y = 4,5
        # ch1,ch2 = a,b
        stack = []
        ans=0
        if(x>y):
            x,y = y,x
            ch1,ch2 = ch2,ch1

        for i in range(len(s)):
            if(stack and s[i]==ch1 and stack[-1]==ch2):
                stack.pop()
                ans+=y
            else:stack.append(s[i])
        
        new_stack = []

        for i in range(len(stack)):
            if(new_stack and stack[i]==ch2 and new_stack[-1]==ch1):
                new_stack.pop()
                ans+=x
            else:new_stack.append(stack[i])
        return ans


    def maximumGain(self, s: str, x: int, y: int) -> int:
        return self.findMaxGain(s,x,y,'a','b')




# time complexity: O(n)
# space complexity: O(n)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        s = input().strip()
        x,y = list(map(int,input().strip().split()))
        print(Solution().maximumGain(s,x,y))