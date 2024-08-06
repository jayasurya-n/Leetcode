class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s)==0):return ""
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expand_palindrome(i,i,s)
            len2 = self.expand_palindrome(i,i+1,s)

            length = max(len1,len2)
            if (length > end-start+1):
                # if(length==len1):
                #     start = i - (length-1)//2
                #     end = i + (length-1)//2
                # elif(length==len2):
                #     start = i - (length//2-1)
                #     end = i + length//2
                start = i - (length-1)//2
                end = i+length//2
        return s[start:end+1]
    
    def expand_palindrome(self,left,right,s):
        while(left>=0 and right<len(s) and s[left]==s[right]):
            left-=1
            right+=1
        return right-left-1



s = input()
print(Solution().longestPalindrome(s))