class Solution:
    def maxDepth(self, s: str) -> int:
        ans  = 0
        cnt = 0
        for i in s:
            if(i=='('):
                cnt+=1
                ans = max(ans,cnt)
            elif(i==')'):cnt-=1
        return ans




s = input()
print(Solution().maxDepth(s))