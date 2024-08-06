class Solution:
    def getParenthesis(self,string,open,close,n,ans):
        if(open+close==2*n):
            ans.append(string)
            return
        if(open<n):self.getParenthesis(string+"(",open+1,close,n,ans)
        if(close<open):self.getParenthesis(string+")",open,close+1,n,ans)

    def generateParenthesis(self, n: int) -> list[str]:
        string = ""
        ans = []
        open, close = 0,0
        self.getParenthesis(string,open,close,n,ans)
        return ans


# time complexity: O(2^n), precisely it is Catalan number O(2nCn)/(n+1)  
# space complexity: O(2n)(recursion stack)
n = int(input())
print(Solution().generateParenthesis(n))