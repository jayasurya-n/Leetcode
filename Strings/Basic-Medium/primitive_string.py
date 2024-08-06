class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt = 0
        ans = ""
        start = 0
        for i in range(len(s)):
            ch = s[i] 
            if(ch=='('):cnt+=1
            elif(ch==')'):cnt-=1
            if(cnt==0):
                ans+= s[start+1:i]
                start = i+1

        return ans

            


s = input().strip()
print(Solution().removeOuterParentheses(s))