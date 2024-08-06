from typing import List
class Solution:
    def checkValidString(self, s: str) -> bool:
        openMin,openMax = 0,0
        for i in range(len(s)):
            if(s[i]=='('):
                openMin+=1
                openMax+=1
            elif(s[i]==')'):
                openMin-=1
                openMax-=1
            else:
                openMax+=1
                openMin-=1
            if(openMax<0):return False
            if(openMin<0):openMin=0
        return openMin==0
            
# time complexity: O(3^k) using recursion
# space complexity: O(k) (stack space)using recursion

# time complexity: O(k) using greedy
# space complexity: O(1) using greedy

if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        s = input().strip()
        print(Solution().checkValidString(s))