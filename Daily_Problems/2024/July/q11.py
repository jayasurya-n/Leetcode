from typing import List,Optional
import sys
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ['']
        for i in range(len(s)):
            if(s[i]=='('):
                stack.append('')
            elif(s[i]==')'):
                substring = stack.pop()
                substring = substring[::-1]
                stack[-1]+= substring
            else:
                stack[-1]+=s[i]
        return stack[0]

                
            


# time complexity: O(n^2)
# space complexity: O(n)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        s = input().strip()
        print(Solution().reverseParentheses(s))