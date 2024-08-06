class Solution:
    def reverseWords(self, s: str) -> str:
        # reversedString = ""
        # start = 0
        # s = s.strip()
        # for i in range(len(s)):
        #     if(s[i]==" " and s[i]!=s[i-1]):
        #         reversedString =  " "+s[start:i]+reversedString
        #         print(start,i)
        #     if(s[i]==" "):start=i+1
            
        
        # reversedString =  s[start:]+reversedString
        # return reversedString

        s = s.strip()
        words = s.split(" ")
        words.reverse()
        reversedString = ' '.join(words)
        return reversedString




s = input()
print(Solution().reverseWords(s))