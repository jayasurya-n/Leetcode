class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        neg = False
        if(s[0]=='-'):neg = True
        if(s[0]=='-' or s[0]=='+'):s = s[1:]

        temp = -1
        for i in range(len(s)):
            if(48<=ord(s[i])<=57):temp = i
            else:break
        
        if(temp==-1):s=0
        else:s = int(s[:temp+1])

        if(neg):s = -s
        if(s<-2**31):s = -2**31
        if(s>=2**31):s = 2**31-1
        return s
        












s = input()
print(Solution().myAtoi(s))