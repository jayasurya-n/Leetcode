class Solution:
    # def romanToInt(self, s: str) -> int:
    #     ans = 0

    #     for i in range(len(s)):
    #         if(s[i]=='I'):
    #             if(i<len(s)-1 and s[i+1]=='V'):ans-=1
    #             elif(i<len(s)-1 and s[i+1]=='X'):ans-=1
    #             else:ans+=1
    #         elif(s[i]=='V'):ans+=5
    #         elif(s[i]=='X'):
    #             if(i<len(s)-1 and s[i+1]=='L'):ans-=10
    #             elif(i<len(s)-1 and s[i+1]=='C'):ans-=10
    #             else:ans+=10
    #         elif(s[i]=='L'):ans+=50
    #         elif(s[i]=='C'):
    #             if(i<len(s)-1 and s[i+1]=='D'):ans-=100
    #             elif(i<len(s)-1 and s[i+1]=='M'):ans-=100
    #             else:ans+=100
    #         elif(s[i]=='D'):ans+=500
    #         elif(s[i]=='M'):ans+=1000
        
    #     return ans
    
    def romanToInt(self, s: str) -> int:
        roman = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for i in range(len(s)):
            if i+1<len(s) and roman[s[i]]<roman[s[i+1]]:
                ans-=roman[s[i]]
            else:ans+=roman[s[i]]
        return ans


s = input()
print(Solution().romanToInt(s))