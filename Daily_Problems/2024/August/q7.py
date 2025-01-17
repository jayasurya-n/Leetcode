from typing import List,Optional
from collections import deque
import sys
class Solution:
    def numberToWords(self, num: int):
        map = {1:"One",2:"Two" ,3:"Three",4:"Four",5:"Five",
               6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",
               11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",
               16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",
               20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",
               70:"Seventy",80:"Eighty",90:"Ninety"}
        
        steps = ["","Thousand","Million","Billion"]
        
        if(num==0):return "Zero"
        final = ""
        i = 0
        while(num)>0:
            if num%1000!=0:
                ans = ""
                part = num%1000
                
                if part>=100:
                    ans+=map[part//100]+" Hundred "
                    part%=100
                
                if part>=20:
                    ans+=map[(part//10)*10]+" "
                    part%=10
                
                if 0<part<20:
                    ans+=map[part]+" "

                ans+=steps[i]+" "
                final = ans+final
            
            i+=1    
            num//=1000
        return final.strip()        
        
# time complexity: O(logN or digits of N)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        num  = int(input().strip())
        print(Solution().numberToWords(num))


# from typing import List,Optional
# from collections import deque
# import sys
# class Solution:
#     def numberToWords(self, num: int):
#         map = {"1":"One","2":"Two" ,"3":"Three","4":"Four","5":"Five",
#                "6":"Six","7":"Seven","8":"Eight","9":"Nine","10":"Ten",
#                "11":"Eleven","12":"Twelve","13":"Thirteen","14":"Fourteen","15":"Fifteen",
#                "16":"Sixteen","17":"Seventeen","18":"Eighteen","19":"Nineteen",
#                "20":"Twenty","30":"Thirty","40":"Forty","50":"Fifty","60":"Sixty",
#                "70":"Seventy","80":"Eighty","90":"Ninety"}
        
#         def solve(s):
#             ans = ""
#             if(len(s)==3):
#                 if(s[0]!="0"):ans+=map[s[0]]+" Hundred"
#                 s = s[1:]
            
#             if(len(s)==2):
                    
#                 if(s in map):
#                     if(ans!=""):ans+=" " 
#                     ans+=map[s]
#                     s=""
#                 else:
#                     if(s[0]!="0"):
#                         if(ans!=""):ans+=" "
#                         ans+=map[s[0]+"0"]
#                     s=s[1:]
            
#             if(len(s)==1):
#                 if(s!="0"):
#                     if(ans!=""):ans+=" "
#                     ans+=map[s]
#             return ans
        
#         if(num==0):return "Zero"
#         num = str(num)
#         step = 0
#         ans = ""
#         while(step<len(num)):
#             new = ""
#             if(step==0):new = solve(num[-3:])
#             else:
#                 new = solve(num[-step-3:-step])
#                 if(new and step==3):new+=" Thousand"
#                 elif(new and step==6):new+=" Million"
#                 elif(new and step==9):new+=" Billion"
            
#             if(ans!="" and new!=""):ans = " "+ans
#             ans = new +ans    
#             step+=3
#         return ans
            

# # time complexity: O(logN or digits of N)
# # space complexity: O(1)